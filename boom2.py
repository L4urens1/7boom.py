import keyboard
import time
import sys ,subprocess
import colorama
from colorama import Back,Style,Fore
colorama.init(autoreset=True)

num = 2

next = "next"
next_bold = f"{Fore.BLACK}{Back.WHITE}next{Back.BLACK}"
on_next = False

boom = "boom"
boom_bold = f"{Fore.BLACK}{Back.WHITE}boom{Back.BLACK}"


print("")

print("_________")
print("        /   |¯¯¯¯¯¯¯¯¯¯\    |¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯|   |\      /|")
print("       /    |           |   |         |   |         |   | \    / |")
print("      /     |          /    |         |   |         |   |  \  /  |")
print("     /      |¯¯¯¯¯¯¯¯¯¯\    |         |   |         |   |   \/   |")
print("    /       |           |   |         |   |         |   |        |")
print("   /        |__________/    |_________|   |_________|   |        |")
print("")
print("")
print(f"                    {Fore.BLACK}{Back.WHITE}press enter to start the game")
while True:
   if keyboard.is_pressed("Enter"):
      subprocess.run('cls',shell=True)
      break
   
print(num)
print(next_bold,boom)
time.sleep(0.5)
while True:

    if keyboard.is_pressed("right") and on_next ==False:
        subprocess.run('cls',shell=True)
        print(num)
        print(next,boom_bold)
        on_next = True

    if keyboard.is_pressed("left") and on_next == True:
        subprocess.run('cls',shell=True)
        print(num)
        print(next_bold,boom)
        on_next = False

    if keyboard.is_pressed("Enter") and on_next == False:
        if num/7 == int(num/7) or "7" in str(num):
            subprocess.run('cls',shell=True)
            print(f"{Fore.RED}no it was boom")
            time.sleep(1)
            subprocess.run('cls',shell=True)
            break

        if num/7 != int(num/7) or "7" not in str(num) :
            subprocess.run('cls',shell=True)
            print(f"{Fore.GREEN}next")
            int(num)
            num += 1
            time.sleep(0.5)
            subprocess.run('cls',shell=True)
            print(num)
            print(next_bold,boom)


    if keyboard.is_pressed("Enter") and on_next == True:

        if num/7 == int(num/7) or "7" in str(num):
            subprocess.run('cls',shell=True)
            print(f"{Fore.GREEN}boom")
            time.sleep(0.5)
            subprocess.run('cls',shell=True)
            
            num +=1
            print(num)
            print(next,boom_bold)

        elif num/7 != int(num/7) or "7" not in str(num):
            subprocess.run('cls',shell=True)
            print(f"{Fore.RED}no it was next")
            time.sleep(1)
            subprocess.run('cls',shell=True)
            break