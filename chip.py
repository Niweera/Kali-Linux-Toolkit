#!/usr/bin/env python

import subprocess
import optparse
import re

def get_args():
	parser = optparse.OptionParser()
	parser.add_option("-i" , "--interface" , dest = "interface" , help = "Interface to change the IP Address")
	parser.add_option("-p" , "--ip" , dest = "ip" , help = "New IP Address")
	parser.add_option("-n" , "--netmask" , dest = "netmask" , help = "New Net Mask")
	(options , arguments) =  parser.parse_args()
	interface = options.interface
	ip = options.ip
	netmask = options.netmask
	if not (interface or ip or netmask):
		parser.error("[-] Please enter both interface and new IP Address and Net Mask, use --help for more information.")
	elif not (interface):
		parser.error("[-] Please enter an interface, use --help for more information.")
	elif not (ip):
		parser.error("[-] Please enter a new IP Address, use --help for more information.")
	elif not (netmask):
		parser.error("[-] Please enter a new Net Mask, use --help for more information.")
	else:
		return options


def ch_mac(interface,ip,netmask):
	print("[+] Changing IP Adreess of " + interface + " to " + ip + " and Net Mask to " + netmask)
	if check_mac(interface):
		get_current_ip(interface)
		subprocess.call(["ifconfig" , interface , ip , "netmask" , netmask])
		check_new_ip(interface)
	else:
		print("[-] The MAC Address can not be read!")

def check_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig" , interface])
	mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , ifconfig_result)
	if mac_result:
		return True
	else:
		return False

def get_current_ip(interface):
	ifconfig_result = subprocess.check_output(["ifconfig" , interface])
	ip_result = re.search(r"(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)" , ifconfig_result) 
	if ip_result:
		print("[+] Current IP Address is " + ip_result.group(0))

def check_new_ip(interface):
	ifconfig_result = subprocess.check_output(["ifconfig" , interface])
	ip_result = re.search(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b" , ifconfig_result)
	if ip_result:
		if  (ip_result.group(0) == options.ip):
			print("[+] The IP Address of the given interface is successfully changed to " + options.ip)
		else:
			print("[-] The IP Address could not be changed!")

options = get_args()
ch_mac(options.interface , options.ip , options.netmask)