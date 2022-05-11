#!/usr/bin/env python3

import csv
import macaddress 

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

def get_unique_ouis(macs_list, ouis_dict):
    """ 
    Weed out duplicates
    """
    unique_ouis = {} 
    for mac_line in macs_list:
        mac_addr = mac_line.strip()
        mac = macaddress.MAC(mac_addr).oui
        oui = str(mac).replace('-', '')
        unique_ouis[ouis_dict[oui]] = oui
    return unique_ouis

def get_corporations(unique_ouis):
    corporations = []
    for key in unique_ouis:
        corporations.append(key)
    corporations.sort()
    return corporations

def print_unique_corporations(corporations):
    for corp in corporations:
        print(corp)

### MAIN ###

# Create a dictionary from a two column CSV file 
ouis_dict = get_dict_from_csv('linux_oui.csv')     

# Create a list from a single column CSV file
macs_list = get_list_from_file('macs.csv')

# Create a dictionary of unique OIDS from the list of MAC addresses
unique_ouis = get_unique_ouis(macs_list, ouis_dict)

# Create a sorted list of all the corporations from the dictionary of unique OIDS
corporations = get_corporations(unique_ouis)

# Print the list of corporations 
print_unique_corporations(corporations)

exit(0)