import  scapy.all as scapy
import optparse as parse
#ARP Address Resoultion Protocol -- Adres Cozumleme Protokolu
#Broadcast Requests  -- Yayin istegi <mac\Ip Adresi eslestirme>
#Response -- tepki saglamak

def get_user_input():
    parse_obcjet = parse.OptionParser()
    parse_obcjet.add_option("-i","--ipaddress",dest="ip_address",help="Please enter a ip address for...This is example help description")
    (user_input,arguments) = parse_obcjet.parse_args()

    if not user_input.ip_address:
        print("Enter ip address !")

    return user_input

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combained_packet = broadcast_packet/arp_request_packet
    (answered_list,unansered_list)= scapy.srp(combained_packet,timeout=1)
    answered_list.summary()

user_ip_address = get_user_input()
scan_my_network(user_ip_address.ip_address)



