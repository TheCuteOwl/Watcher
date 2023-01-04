import requests
from colorama import init
from colorama import Fore, Back, Style
init()
import argparse

# Création de l'analyseur d'arguments
parser = argparse.ArgumentParser()

# Ajout d'un argument nommé "username" à l'analyseur
parser.add_argument("username", help="Username")

# Analyse des arguments
args = parser.parse_args()

# Récupération de la valeur de l'argument "username"
username = args.username

if username is None:
  print("You must put a username after watcher.py")
  input('Press any key to leave...')
  quit()
else:
  print('Checking...')

def check_speedrun_username_availability(username):
  url = f'https://www.speedrun.com/api/v1/users?lookup={username}'
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    if data['data']:
      return False
    else:
      return True
  else:
    raise Exception(f'Unexpected status code: {response.status_code}')


def check_github_username_availability(username):
  url = f'https://api.github.com/users/{username}'
  response = requests.get(url)
  if response.status_code == 200:
    return False
  elif response.status_code == 404:
    return True
  else:
    raise Exception(f'Unexpected status code: {response.status_code}')


def is_minecraft_username_available(username):
  url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
  response = requests.get(url)
  if response.status_code == 204:
    return True
  else:
    return False





def check_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    r = requests.get(url)
    if r.status_code == 404:
      return True
    elif r.status_code == 200:
      return False
    else:
      return False

def check_username_available(username):
    url = f"https://api.roblox.com/users/get-by-username?username={username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    elif response.status_code == 404:
        return True
    else:
        # Some other error occurred
        raise Exception("An error occurred while checking the availability of the username")


if is_minecraft_username_available(username):
  print(Fore.GREEN + f"[+] Minecraft | {username} is avaible.")
else:
  print(Fore.RED + f"[-] Minecraft | {username} is not avaible. | https://namemc.com/profile/{username}")

if check_github_username_availability(username):
  print(Fore.GREEN + f'[+] Github | {username} is available')
else:
  print(Fore.RED + f'[-] Github | {username} is not available. | https://github.com/{username}')

if check_speedrun_username_availability(username):
  print(Fore.GREEN + f'[+] Speedrun.com | {username} is available')
else:
  print(Fore.RED + f'[-] Speedrun.com | {username} is not available.| https://www.speedrun.com/user/{username}')

if check_username_available(username):
    print(Fore.GREEN + f"[+] Roblox {username} is available")
else:
    print(Fore.RED + f"[-] Roblox {username} is not available | https://api.roblox.com/users/get-by-username?username={username}")

input('press enter to quit\n')
