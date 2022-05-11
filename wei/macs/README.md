## Problem 1
Create a CLI script in Python that consumes paths to 2 CSV files as arguments, one
containing a list of MAC addresses and one containing a mapping between MAC OUIs and
Corporation names, and output a CSV that matches MAC addresses to Corporation names
without duplicate MAC entries and sorted alphabetically by corporation name. Input files
should have been emailed to you alongside with this problem set

### Solution
```sh
list_corporation_for_mac.py -o ./linux_oui.csv -m ./macs.csv
```
Creates the file *macs_with_corp_name.csv* as output

### NOTES
I have to use some of the commands listed in *setup.sh* 
to convert macs.csv and oui.csv to be linux friendly.

### Extra
**corporation_from_mac.py**
Prints out all the corporation names founs in the macs.csv file
`
ASUSTek COMPUTER INC.
AXIOM TECHNOLOGY CO., LTD.
Corvalent Corporation
G-PRO COMPUTER
HUGHES NETWORK SYSTEMS
Hewlett Packard
IBM
IBM Corp
Ingenico International
LEXMARK INTERNATIONAL, INC.
OKI ELECTRIC INDUSTRY CO., LTD
PC Partner Ltd.
PRONET GMBH
TRENDnet, Inc.
Toshiba Global Commerce Solutions
Universal Global Scientific Industrial Co., Ltd.
Verifone
Vertical Communications
WINSYSTEMS, INC.
`