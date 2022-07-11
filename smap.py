#!/bin/python3
#coded by U4I5 For pentesting
import nmap3
searchmap = nmap3.Nmap()
#Target Ip address
Ip = input('[+] Target: ')

#Interface
#Iface = input("[+] Iface: ")

# Scan Top 1000 ports with arguments : -Sv -sC 
results = searchmap.scan_top_ports(target=Ip, args="-sV" "-sC")



