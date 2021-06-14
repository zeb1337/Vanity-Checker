import requests
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def checkVanity(vanity):
	r = requests.get(f"https://discordapp.com/api/invites/{vanity}")
	if r.status_code == 200:
		print(f"{Fore.RED}v {Fore.RESET}discord.gg/{vanity} | Taken")
	elif r.status_code == 404:
		print(f"{Fore.GREEN}v {Fore.RESET}discord.gg/{vanity} | Not Taken")

if __name__ == "__main__":
	vanity = input(f"v Vanity: ")
	checkVanity(vanity)