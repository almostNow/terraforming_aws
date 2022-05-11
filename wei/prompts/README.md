# Interview Problem Set Prompt Answers
## Automation Projects
- Automated the software deployment process using Ansible.
- Used Ansible to upgrade Ubuntu 16.04 environments to Ubuntu 20.04.
- Wrote a Python script to create a version number in Jira.
- Created a POC for using Docker and Nexus Repository III with Jenkins.

I enjoyed the POC project the most but I also enjoyed the Ubuntu upgrade because it was challenging.

I chose to pursue the POC because the company had a complex, immutable, and siloed Jenkins build agent architecture. 
I wanted to introduce them to the concept of using Infrastcuture as code with ephemeral Docker build agents. 
I Installed Ubuntu 20.04 on a retired laptop that I took the initiative to obtain from IT to use as a Docker server. I ran Jenkins, Nexus III as Docker containers. I used a Dockerfile and groovy script in a Jenkins file to pull code from git/bitbucket and use a Docker container to build a Rust project.  
The artifacts were then published to the Nexus server/container. The company was using just an open web server to host artifacts so I added Nexus to the process as extra credit. 
I do not have a copy of the code.

## Programming language of choice
I have been drawn to Python mostly for practical reasons.  
The biggest reason being it’s popularity and OO capability.
Golang seems interesting and may be something I look into.

# 5000 Linux based VMs:
I would ask questions to expose the ultimate goal of the systems as well as obtain information as to what resources are available and what are the constraints.
##### Example Questions:
- How time sensitive is the problem? 
- Are they running out of resources?
- What are the VMs being used for? 
- What VM related processes are they using now?
- What existing software development tools are the company using?

The solution recommendation would be to setup an IaC system for provisioning, configuring, and monitoring the VM deployments.
An example of this would be pull the IaC definitions from git and then using Terraform for provisioning and Ansible for configuration management of the VMs. 
The steps of provisioning, configuring, and monitoring the VM deployments should be separated and structured with the goal of keeping the steps decoupled from each other as mush as possible.
I would recommend using Ansible as the configuration management tool because it is agentless and well matured.

## Migrating 10,000 user accounts
I have no experience with Cisco ISE so I looked and found what I believe to be relevant information [here.](https://www.cisco.com/en/US/docs/security/ise/1.0/user_guide/ise10_man_identities.pdf)
I would ask the network engineer if he knows about the ability to export and import user identities as CSV files. I would also ask questions pertaining to creating a way to access the user entities via automation. The engineer will have to setup some sort of access.  Then we can discuss where we would like the user entity CSV resource stored.  Should we keep it in version control?

If it was found that Cisco ISE has functionality via a CLI or API to programmatically access the user entities, I would work to create a script in source code that could export and import the user identities.   

I am not sure of what tools I would use at this point because I have no experience with Cisco ISE.  Python scripting comes to mind first. It would also be nice to create an interface to the automation that allows the network engineer to run the script without having to setup Python.
Perhaps a Python Flask Docker container would do the trick. The network engineer can fill out the required fields in the web interface and click the export or import button.

## Sample Code
I have a small python script [here.](https://github.com/almostNow/peopledatalabs)

## Organization Tools
The companies action item list. One example would be my Jira ticket list.
I like to use a physical notebook to create a daily checklist as well.
I am visual so I like to have access to a white board.
I will keep any personal scripts in a certain structure on my work laptop.  I have been using git lately for that.
