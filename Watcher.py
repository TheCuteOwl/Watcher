import requests
from colorama import init
from colorama import Fore, Back, Style
init()
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("username", help="Le pseudo Minecraft à vérifier")

args = parser.parse_args()

username = args.username

if username is None:
  print("Veuillez fournir un pseudo Minecraft à vérifier.")
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

def twitter(username):
  url = f"https://twitter.com/users/username_available?username={username}"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    return data["valid"]
  else:
    return "Error checking availability"


def flickr(username):
  url = f"https://www.flickr.com/photos/{username}"
  r = requests.get(url)
  if r.status_code == 200:
      return False
  elif r.status_code == 404:
      return True


def check_vimeo_username(username):
  api_url = "https://vimeo.com/api/v2/user/check_username.json"
  params = {"username": username}
  response = requests.get(api_url, params=params)
  if response.status_code == 404:
    return True
  else:
    return False


def patreon(username):
    url = f"https://www.patreon.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def amino(username):
    url = f"https://aminoapps.com/u/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def Itchio(username):
    url = f"https://itch.io/profile/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def dailymotion(username):
    url = f"https://www.dailymotion.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def xvid(username):
    url = f"https://www.xvideos.com/channels/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def soundcloud(username):
    url = f"https://soundcloud.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def etsy(username):
    url = f"https://www.etsy.com/fr/shop/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def deviantart(username):
    url = f"https://www.deviantart.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def behance(username):
    url = f"https://www.behance.net/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def spotify(username):
    url = f"https://open.spotify.com/user/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def Slack(username):
    url = f"https://{username}.slack.com/"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def Gog(username):
    url = f"https://www.gog.com/u/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def Scratch(username):
    url = f"https://scratch.mit.edu/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def Snapchat(username):
    url = f"https://www.snapchat.com/add/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def Dribbble(username):
    url = f"https://dribbble.com/{username}/"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def Myspace(username):
    url = f"https://myspace.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

def producthunt(username):
    url = f"https://www.producthunt.com/@{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return False
    return True

if producthunt(username):
  print(Fore.GREEN + f'[+] Producthunt | {username} | is available.')
else:
  print(Fore.RED + f'[-] Producthunt | {username} | is not available | https://www.producthunt.com/@{username}')

if Myspace(username):
  print(Fore.GREEN + f'[+] Myspace | {username} | is available.')
else:
  print(Fore.RED + f'[-] Myspace | {username} | is not available | https://myspace.com/{username}')

if Dribbble(username):
  print(Fore.GREEN + f'[+] Dribbble | {username} | is available.')
else:
  print(Fore.RED + f'[-] Dribble | {username} | is not available | https://dribbble.com/{username}/')

if Snapchat(username):
  print(Fore.GREEN + f'[+] Snapchat | {username} | is available.')
else:
  print(Fore.RED + f'[-] Snapchat | {username} | is not available | https://www.snapchat.com/add/{username}')

if Scratch(username):
  print(Fore.GREEN + f'[+] Scratch | {username} | is available.')
else:
  print(Fore.RED + f'[-] Scratch | {username} | is not available | https://scratch.mit.edu/users/{username}')

if Gog(username):
  print(Fore.GREEN + f'[+] Gog | {username} | is available.')
else:
  print(Fore.RED + f'[-] Gog | {username} | is not available | https://www.gog.com/u/{username}')

if Slack(username):
  print(Fore.GREEN + f'[+] Slack | {username} | is available.')
else:
  print(Fore.RED + f'[-] Slack | {username} | is not available | https://{username}.slack.com/')

if spotify(username):
  print(Fore.GREEN + f'[+] Spotify | {username} | is available.')
else:
  print(Fore.RED + f'[-] Spotify | {username} | is not available | https://open.spotify.com/user/{username}')

if behance(username):
  print(Fore.GREEN + f'[+] Behance | {username} | is available.')
else:
  print(Fore.RED + f'[-] Behance | {username} | is not available | https://www.behance.net/{username}')

if deviantart(username):
  print(Fore.GREEN + f'[+] DeviantArt | {username} | is available.')
else:
  print(Fore.RED + f'[-] DeviantArt | {username} | is not available | https://www.deviantart.com/{username}')

if etsy(username):
  print(Fore.GREEN + f'[+] Etsy | {username} | is available.')
else:
  print(Fore.RED + f'[-] Etsy | {username} | is not available | https://www.etsy.com/fr/shop/{username}')

if soundcloud(username):
  print(Fore.GREEN + f'[+] Soundcloud | {username} | is available.')
else:
  print(Fore.RED + f'[-] Soundcloud | {username} | is not available | https://soundcloud.com/{username}')

if xvid(username):
  print(Fore.GREEN + f'[+] xvideos | {username} | is available.')
else:
  print(Fore.RED + f'[-] xvideos | {username} | is not available | https://www.xvideos.com/channels/{username}')

if dailymotion(username):
  print(Fore.GREEN + f'[+] Dailymotion | {username} | is available.')
else:
  print(Fore.RED + f'[-] Dailymotion | {username} | is not available | https://www.dailymotion.com/{username}')

if Itchio(username):
  print(Fore.GREEN + f'[+] Itch.io | {username} | is available.')
else:
  print(Fore.RED + f'[-] Itch.io | {username} | is not available | https://itch.io/profile/{username}')

if amino(username):
  print(Fore.GREEN + f'[+] Amino | {username} | is available.')
else:
  print(Fore.RED + f'[-] Amino | {username} | is not available | https://aminoapps.com/u/{username}')

if patreon(username):
    print(Fore.GREEN + f"[+] Patreon | {username} | is available.")
else:
    print(Fore.RED + f"[-] Patreon | {username} | is not available | https://www.patreon.com/{username}")

vimeo = check_vimeo_username(username)

if vimeo:
  print(Fore.GREEN + f"[+] Vimeo | {username} | is available.")
else:
  print(Fore.RED + f"[-] Vimeo | {username} | is not available. | https://vimeo.com/{username}")

if flickr(username):
  print(Fore.GREEN + f"[+] Flickr | {username} | is avaible.")
else:
  print(Fore.RED + f"[-] flickr | {username} | is not avaible. | https://www.flickr.com/photos/{username}")

if is_minecraft_username_available(username):
  print(Fore.GREEN + f"[+] Minecraft | {username} | is avaible.")
else:
  print(Fore.RED + f"[-] Minecraft | {username} | is not avaible. | https://namemc.com/profile/{username}")

if check_github_username_availability(username):
  print(Fore.GREEN + f'[+] Github | {username} | is available')
else:
  print(Fore.RED + f'[-] Github | {username} | is not available. | https://github.com/{username}')

if check_speedrun_username_availability(username):
  print(Fore.GREEN + f'[+] Speedrun.com {username} | is available')
else:
  print(Fore.RED + f'[-] Speedrun.com | {username} | is not available.| https://www.speedrun.com/user/{username}')


input('press enter to quit\n')
