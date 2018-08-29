#!/usr/bin/env python

import subprocess
import optparse
import re

def get_args():
	parser = optparse.OptionParser()
	parser.add_option("-i" , "--interface" , dest = "interface" , help = "Interface to change the MAC Address")
	parser.add_option("-m" , "--mac" , dest = "mac" , help = "New MAC Address")
	(options , arguments) =  parser.parse_args()
	interface = options.interface
	mac = options.mac
	if not (interface or mac):
		parser.error("[-] Please enter both interface and new MAC Address, use --help for more information.")	
	elif not (interface):
		parser.error("[-] Please enter an interface, use --help for more information.")
	elif not (mac):
		parser.error("[-] Please enter a new MAC Address, use --help for more information.")
	else:
		return options


def ch_mac(interface,new_mac):
	print("[+] Changing MAC Adreess of " + interface + " to " + new_mac)
        if check_mac(interface):
		get_current_mac(interface)
		subprocess.call(["ifconfig" , interface , "down"])
		subprocess.call(["ifconfig" , interface , "hw", "ether" , new_mac])
		subprocess.call(["ifconfig" , interface , "up"])
		check_new_mac(interface)
	else:
		print("[-] The MAC Address can not be read!")


def check_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig" , interface])
        mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , ifconfig_result)
        if mac_result:
	        return True
        else:
                return False

def get_current_mac(interface):
        ifconfig_result = subprocess.check_output(["ifconfig" , interface])
        mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , ifconfig_result)
        if mac_result:
	        print("[+] Current MAC Address is " + mac_result.group(0))	

def check_new_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig" , interface])
        mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , ifconfig_result)
        if mac_result:
                if  (mac_result.group(0) == options.mac): 
                        print("[+] The MAC Address of the given interface is successfully changed to " + options.mac)
                else:
                        print("[-] The MAC Address could not be changed!")

options = get_args()
ch_mac(options.interface , options.mac)

