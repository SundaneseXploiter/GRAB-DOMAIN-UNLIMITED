#Author SUSUDOSU

import requests
import os
import socket
import sys
from bs4 import BeautifulSoup
import time
import re
from colorama import Fore, Style, init

def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')
        
def banners():
    clear_screen()
    # Display the ASCII art banner
    print("                                                                                         ")
    print(Fore.RED + "_______ _______ _______ _____  _______ _______ _______ _______ _______  ")
    print(Fore.RED + "|     __|   |   |    |  |     \|   _   |    |  |    ___|     __|    ___|")
    print(Fore.WHITE + "|__     |   |   |       |  --  |       |       |    ___|__     |    ___|")
    print(Fore.WHITE + "|_______|_______|__|____|_____/|___|___|__|____|_______|_______|_______|")
    print(Fore.RED + f"════════════╦══════════════════════════════════════════════╦════════════")
    # Display additional information about the host/device
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print(Fore.RED + f"╔═══════════╩══════════════════════════════════════════════╩═══════════╗")
    print(Fore.LIGHTGREEN_EX + f"                   [ UNLIMITED SCRAPE DOMAIN TLD ]            ")
    print(Fore.RED + f"╚══════════════════════════════════════════════════════════════════════╝")
    print(Fore.RED + f"[ ! ]{Fore.RESET} Author: {Fore.LIGHTRED_EX}SUSUDOSU {Fore.LIGHTGREEN_EX}EST - 2023")
    print(f"{Fore.GREEN}[ {Fore.RED}! {Fore.GREEN}]{Fore.RESET} Device: {host_name}")
    print(f"{Fore.GREEN}[ {Fore.RED}! {Fore.GREEN}]{Fore.RESET} Host  : {ip_address}")
    print(Fore.RED + f"════════════════════════════════════════════════╝")
    
def get_domains(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'table-bordered'})

    domains = [re.sub(r'^\d+[:.\s]*', '', row.find_all('td')[0].text) for row in table.find_all('tr')[1:]]

    return domains

def save_to_file(domains, filename):
    with open(filename, 'a') as f:
        for domain in domains:
            f.write(domain + '\n')

def scrape_for_tld(tld):
    base_url = f'https://www.topsitessearch.com/domains/{tld}/'
    output_file = f'salindomain_{tld}.txt'
    page = 1

    while True:
        print(f'{Fore.LIGHTRED_EX}[ {Fore.LIGHTGREEN_EX}+ {Fore.LIGHTRED_EX}] {Fore.LIGHTWHITE_EX}Memproses halaman {Fore.LIGHTRED_EX}{page} {Fore.LIGHTWHITE_EX}untuk TLD: {Fore.LIGHTGREEN_EX}{tld}')

        url = base_url + f'{page}/'
        domains = get_domains(url)

        if not domains:
            print(f'{Fore.RED}[ {Fore.LIGHTRED_EX}- {Fore.RED}] {Fore.LIGHTWHITE_EX}Tidak ada domain lebih lanjut untuk TLD: {Fore.LIGHTRED_EX}{tld}')
            break

        for i, domain in enumerate(domains, start=1):
            print(f" {Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTWHITE_EX}] {domain}")

        save_to_file(domains, output_file)
        page += 1
        time.sleep(1)  

def main():
    banners()
    tld_input = input(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTGREEN_EX}+ {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTWHITE_EX}Masukkan TLD atau nama file TLD (misalnya, tlds.txt): ")

    if tld_input.endswith('.txt'):
        try:
            with open(tld_input, 'r') as file:
                tlds = file.read().split()
        except FileNotFoundError:
            print(f"File {tld_input} tidak ditemukan. Pastikan file berada di direktori yang benar.")
            return
    else:
        tlds = [tld_input]

    for tld in tlds:
        scrape_for_tld(tld)

if __name__ == '__main__':
    main()
