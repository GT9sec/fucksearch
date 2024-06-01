import os
import requests
import time
import socket
os.system('clear')
print("\033[1;31;33m ______ _    _  _____ _  __                 \003")
print("\033[1;31;33m |  ____| |  | |/ ____| |/ /                  \003")
print("\033[1;31;33m | |__  | |  | | |    | ' /                   \003")
print("\033[1;31;33m |  __| | |  | | |    |  <                    \003")
print("\033[1;31;33m | |    | |__| | |____| . \                   \003")
print(" \033[1;31;24m|_|____ \____/ \_____|_|\_\__   _____ _    _ \003")
print("\033[1;31;40m  / ____|  ____|   /\   |  __ \ / ____| |  | |\003")
print("\033[1;31;40m | (___ | |__     /  \  | |__) | |    | |__| |\003")
print("\033[1;31;40m  \___ \|  __|   / /\ \ |  _  /| |    |  __  |\003")
print("\033[1;31;40m  ____) | |____ / ____ \| | \ \| |____| |  | |\003")
print("\033[1;31;40m |_____/|______/_/    \_\_|  \_\\_____ |_|  |_|\003")
print("                                               beta(1.0)   [By GT9]")
print("                                              fuck you admin! [team: skull6net]")

def fuck_search(url, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            directory = line.strip()
            url_foda = f"{url}/{directory}"
            if not url_foda.startswith("http"):
                url_foda = f"http://{url_foda}"
            response = requests.get(url_foda)

            if response.status_code == 200:
                print(f"\033[7;31;40mDiretorio encontrado: {url_foda}\033[n")

if __name__ == "__main__":
    target_url = input("\033[1;31;40mDigite a url: \003")

    wordlist_file = input("\033[1;31;33mDigite o caminho da sua wordlist: \003")

    fuck_search(target_url, wordlist_file)
