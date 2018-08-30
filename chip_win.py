#This program is to change the ip address and the net mask of a given interface in windows systems

import subprocess #Importing the module subprocess | subprocess is used to run system commands
import optparse #Importing the module optparse | optparse is used to create parameters, arguments based commands
import re #Importing the re | regular expressions module

#Function to get arguments from the command line

def get_args():
	parser = optparse.OptionParser()
	parser.add_option("-i" , "--interface" , dest = "interface" , help = "Interface to change the IP Address")
	parser.add_option("-p" , "--ip" , dest = "ip" , help = "New IP Address")
	parser.add_option("-n" , "--netmask" , dest = "netmask" , help = "New Net Mask")
	(options , arguments) =  parser.parse_args()
	interface = options.interface
	ip = options.ip
	netmask = options.netmask
	
	#Check whether all the given parameters are given or not

	if not (interface or ip or netmask):
		parser.error("[-] Please enter interface and new IP Address and Net Mask, use --help for more information.")
	elif not (interface):
		parser.error("[-] Please enter an interface, use --help for more information.")
	elif not (ip):
		parser.error("[-] Please enter a new IP Address, use --help for more information.")
	elif not (netmask):
		parser.error("[-] Please enter a new Net Mask, use --help for more information.")
	else:
		return options

#Function to change the interface, ip address and net mask
#Only this function has an else clause since in this function:
#check_mac() function checks whether the given interface is a:
#valid interface or not.
#If the given interface is not valid then the program stops.

def ch_mac(interface,ip,netmask):
	#if check_mac(interface) or True:
	if True:
		#print("[+] Changing IP Address of " + interface + " to " + ip + " and Net Mask to " + netmask)
		#get_current_ip(interface)
		#subprocess.call(["ifconfig" , interface , ip , "netmask" , netmask])
		#check_new_ip(interface)
		subprocess.call(["netsh" , "interface" ,  "ipv4" ,  "show" , "config", "name","=",interface], shell=True)
	else:
		print("[-] The MAC Address can not be read!")

#Function to check the given interface has a mac address or not:
#If there is no mac address for the given interface then return false.

def check_mac(interface):
	ifconfig_result = subprocess.check_output(["netsh" , "interface" ,  "ipv4" ,  "show" , "config", "name","=","Wi-Fi"], shell=True)
	mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , ifconfig_result)
	if mac_result:
		return True
	else:
		return False

#Function to get the current ip address and the net mask of the system

def get_current_ip(interface):
	ip_result = get_ip_result(interface) 
	if ip_result:
		print("[+] Current IP Address is " + ip_result[0] + " and Net Mask is " + ip_result[1])

#Function to check whether the ip address and the net mask is changed:
#to for the given interface.
#If the ip address and net mask is not changed then the error:
#message is displayed.

def check_new_ip(interface):
	ip_result = get_ip_result(interface)
	if ip_result:
		if  (ip_result[0] == options.ip) and (ip_result[1] == options.netmask):
			print("[+] New IP Address is " + options.ip + " and Net Mask is " + options.netmask) 
		else:
			print("[-] The IP Address could not be changed!")

#Function to get the regular expression result for the given pattern
#Returns the result of the regex

def get_ip_result(interface):
	ifconfig_result = subprocess.check_output(["ifconfig" , interface])
	ip_result = re.findall(r"(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)" , ifconfig_result)
	return ip_result

#Calling the function get_args()

options = get_args()

#Calling the function ch_mac()

ch_mac(options.interface , options.ip , options.netmask)