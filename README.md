# MAC-Changer
A simple python program to spoof(cuz it's permanent) the MAC address of any interface.

### ** This script has configured and written in python2.7.x **

## What is a MAC address?
A media access control address (MAC address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment. This use is common in most IEEE 802 networking technologies, including Ethernet, Wi-Fi, and most commonly Bluetooth

## Wanna know what's your MAC address? Use ifconfig + [interface]
 ![Screenshot_2021-04-01_21_13_27](https://user-images.githubusercontent.com/59832397/113319668-52648f00-932f-11eb-8245-d10da8e4ac02.png)

### ether xx:xx:xx:xx:xx:xx is your MAC address

## How to run?
### python -i [interface] -m [mac-address]
 
 *  -i or --interface
 *  -m or --mac 
 
### Interface options?
 * eth0 [Ethernet] (Most probably eth0 please check using ifconfig)
 * wlan0 [Wireless LAN] (Most probably wlan0 please check using ifconfig)

## Looking for reasons to Spoof MAC?

   * **Static IP Assignment**: Routers allow you to assign static IP addresses to your computers. When a device connects, it always receives a specific IP address if it has a matching MAC address
   * **MAC Address Filtering**: Networks can use MAC address filtering, only allowing devices with specific MAC addresses to connect to a network. This isn’t a great security tool because people can spoof their MAC addresses (Like us).
   * **MAC Authentication**: Some Internet service providers may require authentication with a MAC address and only allow a device with that MAC address to connect to the Internet. You may need to change your router or computer’s MAC address to connect.
   * **Device Identification**: Many airport Wi-Fi networks and other public Wi-Fi networks use a device’s MAC address to identify it. For example, an airport Wi-Fi network might offer a free 30 minutes and then ban your MAC address from receiving more Wi-Fi. Change your MAC address and you could get more Wi-Fi. (Free, limited Wi-Fi may also be tracked using browser cookies or an account system.)
   * **Device Tracking**: Because they’re unique, MAC addresses can be used to track you. When you walk around, your smartphone scans for nearby Wi-Fi networks and broadcasts its MAC address. A company named Renew London used trash bins in the city of London to track people’s movements around the city based on their MAC addresses.

### Seriously? You read that shit?.

### Like my work?
### Buy me a pizza.I love them.
https://www.buymeacoffee.com/rootx
