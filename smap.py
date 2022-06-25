#!/bin/python3
#coded by U4I5 For pentesting
import os
import nmap3 
n3 = nmap3.Nmap()
#Target Ip address
Iptarget = input('[+] Target: ')
#Interface
Iface = input("[+] Iface: ")

if Iface == 0:
    Iface = "eth0"

kali = os.system
#1- fast Scan nmap
kali(n3 + "-sV" + "-sC" + "T4" + Iptarget)

#2- Full Scan nmap  
kali(n3 + "-p-" "-sV" + "-sC" + "T4" + Iptarget + "-oN" + Iptarget.txt)
