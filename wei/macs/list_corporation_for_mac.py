#!/usr/bin/env python3

import argparse
import csv
import macaddress 

def get_args():
    parser = argparse.ArgumentParser(description="Corporation for list of MACs",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-m", "--macs", help="Complete file path to MAC addresses CSV file")
    parser.add_argument("-o", "--ouis", help="Complete file path to OUI CSV file")
    args = parser.parse_args()
    return vars(args)

def get_list_from_file(list_file):
    list_from_file = []
    txt_file = open(list_file, "r")
    list_from_file = txt_file.readlines()
    return list_from_file
    
def get_dict_from_csv(csv_file):
    dict_from_csv = {}
    with open(csv_file, mode='r') as inp:
        reader = csv.reader(inp)
        dict_from_csv = {rows[0]:rows[1] for rows in reader}
    return dict_from_csv 

def create_mac_to_corpname_dict(macs_list, ouis_dict):
    mac_to_corpname_dict = {}
    for mac_line in macs_list:
        mac_addr = mac_line.strip()
        mac = macaddress.MAC(mac_addr).oui
        oui = str(mac).replace('-', '')
        mac_to_corpname_dict[mac_addr] = ouis_dict[oui]
    return mac_to_corpname_dict

def create_csv_file(mac_to_corpname_dict):
    sort_by_corp = sorted(mac_to_corpname_dict.items(), key=lambda x: x[1])

    f = open('./macs_with_corp_name.csv', 'w', encoding='UTF8')
    writer = csv.writer(f)
    header = ['MAC','Corporation']
    writer.writerow(header)

    for i in sort_by_corp:
        writer.writerow(i)

    f.close()
### MAIN ###

# Get the arguments passed into the script
config = get_args()

# Create a dictionary from a two column CSV file 
ouis_dict = get_dict_from_csv(config['ouis'])     

# Create a list from a single column CSV file
macs_list = get_list_from_file(config['macs'])

mac_to_corpname_dict = create_mac_to_corpname_dict(macs_list, ouis_dict)

create_csv_file(mac_to_corpname_dict)

exit(0)