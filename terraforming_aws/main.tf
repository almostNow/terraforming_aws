resource "aws_vpc" "egj_vpc" {
  cidr_block           = "10.123.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "dev"
  }
}

resource "aws_subnet" "egj_public_subnet" {
  vpc_id                  = aws_vpc.egj_vpc.id
  cidr_block              = "10.123.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-2a"

  tags = {
    Name = "dev-public"
  }
}

resource "aws_internet_gateway" "egj_internet_gateway" {
  vpc_id = aws_vpc.egj_vpc.id

  tags = {
    Name = "dev-igw"
  }
}

resource "aws_route_table" "egj_public_rt" {
  vpc_id = aws_vpc.egj_vpc.id

  tags = {
    Name = "dev-public-rt"
  }
}

resource "aws_route" "default_route" {
  route_table_id         = aws_route_table.egj_public_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.egj_internet_gateway.id
}

resource "aws_route_table_association" "egj_public_assoc" {
  subnet_id      = aws_subnet.egj_public_subnet.id
  route_table_id = aws_route_table.egj_public_rt.id
}

resource "aws_security_group" "egj_sg" {
  name        = "dev-sg"
  description = "Dev Security Group"
  vpc_id      = aws_vpc.egj_vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["73.89.65.153/32"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "egj_auth" {
  key_name   = "egjkey"
  public_key = file("~/.ssh/egjkey.pub")
}

resource "aws_instance" "dev-node" {
  ami                    = data.aws_ami.server_ami.id
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.egj_auth.id
  vpc_security_group_ids = [aws_security_group.egj_sg.id]
  subnet_id              = aws_subnet.egj_public_subnet.id
  user_data              = file("./userdata.tpl")
  count                  = 2

  root_block_device {
    volume_size = 10
  }

  tags = {
    Name = "dev-node-${count.index}"
  }

  provisioner "local-exec" {
    command = templatefile("linux-ssh-config.tpl", {
      hostname     = self.public_ip,
      user         = "ubuntu",
      identityfile = "~/.ssh/egjkey"
    })
    interpreter = ["bash", "-c"]
  }
}