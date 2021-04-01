#!/usr/bin/env python

# Changes MAC address for selected interface

# Importing modules
import subprocess
#For executing system commands
import optparse
#For parsing the arguments specified
import re
#For regular expressions(regex)

def get_arguments():
    # Use OptionParser class to allow the use of arguments in our program
    parser = optparse.OptionParser()
    # Use arguments for user input for more secure input
    # Here parser is an object and add_option() is a method
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    # Parse the arguments for previous options
    (options, arguments) = parser.parse_args()
    # Code to check for input for each argument. If there's no input, throw an error saying that
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info")
    # Return the options so that it can be read by the other functions also.
    return options


def changing_the_mac(interface, new_mac):
    # Allowing python to execute terminal commands to change the MAC address
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    #subprocess.call allows to execute terminal commands in the background
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_the_current_mac(interface):
    # Here we use regex to print out just the MAC address from the result of ifconfig
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # '\w' is for alphanumeric digits, written with colon to print our MAC
    # Wanna practice regex? Check out https://pythex.org/
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    #Code to check for result exists. If there's no result, throw an error saying that
    if mac_result:
        return mac_result.group(0) 
        #group() attribute if there is more than one match of the string and will be placed in group() and can iterate through 0 to 3
        # But we are usually interested in first occurence so anyway 0.
    else:
        print("[-] Could not read MAC address")


# Main code for program
# Capturing the returned value from get_arguments()
options = get_arguments()

#Print Current MAC
current_mac = get_the_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

# Calling changing_the_mac
changing_the_mac(options.interface, options.new_mac)

current_mac = get_the_current_mac(options.interface)
# Code to check whether MAC address has changed or not. If not throw an error as
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] Mac address did not get changed.")


#Thank you for reading it :)