#!/bin/python3

#coded by U4I5 For my pentesting
import os
#import nmap as n

#Target Ip address
Iptarget = input('[+] Target: ')
#Interface
Iface = input("[+] Iface: ")

if Iface == 0:
    Iface = "eth0"

kali = os.system
#1- fast Scan nmap
kali(nmap + "-sV" + "-sC" + "T4" + Iptarget)

#2- Full Scan nmap  
kali(nmap + "-p-" "-sV" + "-sC" + "T4" + Iptarget + "-oN" + Iptarget.txt)
