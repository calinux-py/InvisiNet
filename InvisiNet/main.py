import scapy.all as scapy
import time
import netifaces as ni
import ipaddress
import pygame

def get_network_range():
    interfaces = ni.interfaces()
    for interface in interfaces:
        addrs = ni.ifaddresses(interface)
        if ni.AF_INET in addrs:
            ip_info = addrs[ni.AF_INET][0]
            ip = ip_info['addr']
            netmask = ip_info['netmask']
            network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
            return str(network)
    return None

def scan_network(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    devices = set()
    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices.add((device_info["ip"], device_info["mac"]))
    return devices

def play_alert_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("audio/NewDevice.mp3")
    pygame.mixer.music.play()

def load_friendly_macs():
    with open('config/mac.ini', 'r') as file:
        friendly_macs = set(line.strip() for line in file)
    return friendly_macs

def main():
    printed_devices = set()
    friendly_macs = load_friendly_macs()
    ip_range = get_network_range()
    if ip_range:
        print(f"\n[ + ] Detected network range: {ip_range}")
        print("[ ~ ] Scanning network. This may take a while...\n")
        pygame.mixer.init()
        pygame.mixer.music.load("audio/scan.mp3")
        pygame.mixer.music.play()
        initial_devices = scan_network(ip_range)
        for ip, mac in initial_devices:
            if (ip, mac) not in printed_devices:
                print(f"\033[92m[ + ] IP Address: {ip}, MAC Address: {mac}\033[0m")
                printed_devices.add((ip, mac))

        grace_start_time = time.time()
        while time.time() - grace_start_time < 10:
            new_devices_during_grace = scan_network(ip_range)
            for ip, mac in new_devices_during_grace:
                if (ip, mac) not in printed_devices:
                    if mac in friendly_macs:
                        print(f"\033[92m[ + ] Friendly device detected: IP Address: {ip}, MAC Address: {mac}\033[0m")
                        print(f"Welcome back, device {mac}!")
                    else:
                        print(f"\033[92m[ + ] IP Address: {ip}, MAC Address: {mac}\033[0m")
                    printed_devices.add((ip, mac))
            time.sleep(1)

        print("\n[ ~ ] Monitoring for new devices...")
        pygame.mixer.init()
        pygame.mixer.music.load("audio/com.mp3")
        pygame.mixer.music.play()
        while True:
            new_devices = scan_network(ip_range)
            new_entries = new_devices - initial_devices
            for ip, mac in new_entries:
                if (ip, mac) not in printed_devices:
                    if mac in friendly_macs:
                        print(f"\n\033[92m[ + ] Friendly device detected: IP Address: {ip}, MAC Address: {mac}\033[0m")
                        print(f"Welcome back, device {mac}!")
                    else:
                        print(f"\n\033[91m[ ! ] ALERT: New device(s) detected:")
                        print(f"[ ! ] IP Address: {ip}, MAC Address: {mac}\033[0m")
                        printed_devices.add((ip, mac))
                        play_alert_sound()
            initial_devices.update(new_entries)
            time.sleep(1)
    else:
        print("No suitable network interface found.")

if __name__ == "__main__":
    main()
