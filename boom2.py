import keyboard
import time
import sys ,subprocess
import colorama
from colorama import Back,Style,Fore
colorama.init(autoreset=True)

num = 1

next = "next"
next_bold = f"{Fore.BLACK}{Back.WHITE}next{Back.BLACK}"
on_next = True

boom = "boom"
boom_bold = f"{Fore.BLACK}{Back.WHITE}boom{Back.BLACK}"
esy = True

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
   
print("what mode do you want to play ?")
print("1- easy")
print("2- hard")

while True:
    a = input()
    if a == "1":
        esy = True
        break
    elif a == "2":
        esy = False
        break

subprocess.run('cls',shell=True)

if esy:      
    print(num)
print(next_bold,boom)

time.sleep(0.5)
# easy mode
while esy:
    # print boom bold if pressed right on next
    if keyboard.is_pressed("right") and on_next ==True:
        subprocess.run('cls',shell=True)
        print(num)
        print(next,boom_bold)
        on_next = False
    # print next bold if pressed left on boom
    if keyboard.is_pressed("left") and on_next == False:
        subprocess.run('cls',shell=True)
        print(num)
        print(next_bold,boom)
        on_next = True
    # check if the answer is right or wrong on next
    if keyboard.is_pressed("Enter") and on_next == True:
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

    # check if the answer is right or wrong on boom
    if keyboard.is_pressed("Enter") and on_next == False:

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
# hard mode
while not esy:
    # print boom bold if pressed right on next
    if keyboard.is_pressed("right") and on_next ==True:
        subprocess.run('cls',shell=True)
        
        print(next,boom_bold)
        on_next = False
    # print next bold if pressed left on boom
    if keyboard.is_pressed("left") and on_next == False:
        subprocess.run('cls',shell=True)
        
        print(next_bold,boom)
        on_next = True
    # check if the answer is right or wrong on next
    if keyboard.is_pressed("Enter") and on_next == True:
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
            
            print(next_bold,boom)

    # check if the answer is right or wrong on boom
    if keyboard.is_pressed("Enter") and on_next == False:

        if num/7 == int(num/7) or "7" in str(num):
            subprocess.run('cls',shell=True)
            print(f"{Fore.GREEN}boom")
            time.sleep(0.5)
            subprocess.run('cls',shell=True)
            
            num +=1
            
            print(next,boom_bold)

        elif num/7 != int(num/7) or "7" not in str(num):
            subprocess.run('cls',shell=True)
            print(f"{Fore.RED}no it was next")
            time.sleep(1)
            subprocess.run('cls',shell=True)
            break