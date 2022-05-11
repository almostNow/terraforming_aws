#!/usr/bin/env bash

python3 -m venv env

sudo apt -y install python3-pip dos2unix

pip3 install macaddress

dos2unix macs.csv

# Converted oui.csv to oui_utf8.csv on Windows with Notepad++

iconv -f WINDOWS-1251 -t UTF-8 oui.csv | dos2unix > linux_oui.csv

cat << EOF 

Run the command below to activate the py virtual env.

$ source ./env/bin/activate

EOF