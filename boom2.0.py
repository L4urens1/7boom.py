import keyboard
import time
import sys ,subprocess
import colorama
from colorama import Back,Style,Fore
colorama.init(autoreset=True)



num = 1


n = "next"
nb = f"{Back.WHITE}next{Back.BLACK}"
nl = False

b = "boom"
bb = f"{Back.WHITE}boom{Back.BLACK}"
nr = True

print("_________")
print("        /   |¯¯¯¯¯¯¯¯¯¯\    |¯¯¯¯¯¯¯¯¯|   |¯¯¯¯¯¯¯¯¯|   |\      /|")
print("       /    |           |   |         |   |         |   | \    / |")
print("      /     |          /    |         |   |         |   |  \  /  |")
print("     /      |¯¯¯¯¯¯¯¯¯¯\    |         |   |         |   |   \/   |")
print("    /       |           |   |         |   |         |   |        |")
print("   /        |__________/    |_________|   |_________|   |        |")
print("")
print("")
print(f"                    {Back.WHITE}press enter to start the game")
while n:
   if keyboard.is_pressed("Enter"):
      subprocess.run('cls',shell=True)
      break
   
print(num)
print(nb,b)
time.sleep(0.5)
while True:


    if keyboard.is_pressed("right") and nl ==False:
        subprocess.run('cls',shell=True)
        print(num)
        print(n,bb)
        nl = True
        br = False 
    if keyboard.is_pressed("left") and nl == True:
        subprocess.run('cls',shell=True)
        print(num)
        print(nb,b)
        nl = False
        br = True


    if keyboard.is_pressed("Enter") and nl == False:
        if num/7 == int(num/7) or "7" in str(num):
            subprocess.run('cls',shell=True)
            print(f"{Fore.RED}no it was boom")
            time.sleep(1.5)
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
            print(nb,b)


    if keyboard.is_pressed("Enter") and nl == True:



        if num/7 == int(num/7) or "7" in str(num):
            subprocess.run('cls',shell=True)
            print(f"{Fore.GREEN}boom")
            time.sleep(0.5)
            subprocess.run('cls',shell=True)
            
            num +=1
            print(num)
            print(n,bb)

        elif num/7 != int(num/7) or "7" not in str(num):
            subprocess.run('cls',shell=True)
            print(f"{Fore.RED}no it was next")
            time.sleep(1.5)
            subprocess.run('cls',shell=True)
            break