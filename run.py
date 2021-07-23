#!/usr/bin/python3
# This Programm Write by Mr.nope
# Instagram Upload v1.2
import getpass
import os, time, sys, platform
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip3 install colorama")
try:
    from instabot import Bot
except ImportError:
    os.system("pip install instabot")
system = platform.uname()[0]
End = '\033[0m'
opt = Fore.GREEN + "\nchoose/>" + End
org = '\033[33m'
run_Err = "\nThis Programm can run on Windows, Linux, MacOS!\n"
banner = Fore.LIGHTGREEN_EX + """
██    ██ ██████  ██       ██████   █████  ██████  ███████ ██████  
██    ██ ██   ██ ██      ██    ██ ██   ██ ██   ██ ██      ██   ██  """ + Fore.RED + "Version: " + org + "1.2" + Fore.LIGHTGREEN_EX + """
██    ██ ██████  ██      ██    ██ ███████ ██   ██ █████   ██████  
██    ██ ██      ██      ██    ██ ██   ██ ██   ██ ██      ██   ██ 
 ██████  ██      ███████  ██████  ██   ██ ██████  ███████ ██   ██ 
                                                                  
                                    """ + End

def title():
    if system == 'Linux':
        os.system("printf '\033]2;Uploader\a'")
    elif system == 'Windows':
        os.system("title Uploader")
    else:
        print(run_Err)
        sys.exit()
def cls():
    if system == 'Windows':
        os.system("cls")
    elif system == 'Linux':
        os.system("clear")
    else:
        print(run_Err)
        sys.exit()
def ext():
    cls()
    print(Fore.GREEN + "Exiting..." + End)
    sys.exit()
def main():
    title()
    cls()
    print(banner)
    print("\n{1}.Start")
    print("{2}.Exit")
    choose = input(opt)
    if choose == '1':
        start()
    elif choose == '2':
        ext()
    else:
        main()
def start():
    cls()
    run = Bot()
    user = input("\nEnter UserName: ")
    time.sleep(0.50)
    pass_ = getpass.getpass("\nEnter Password: ")
    time.sleep(0.25)
    pictures = input("\nEnter Pictures: ")
    time.sleep(0.25)
    caption = input("\nCaption: ")
    time.sleep(0.15)
    run.login(username = user,password = pass_)
    run.upload_photo(pictures,caption = caption)
    time.sleep(1)
    try1()
def try1():
    try_again = input("\nDo you want to try again? [y/n] ")
    if try_again == 'y':
        start()
    elif try_again == 'n':
        try2()
    else:
        try1()
def try2():
    try_to_menu = input("\nDo you want to Back Main Menu? [y/n] ")
    if try_to_menu == 'y':
        main()
    elif try_to_menu == 'n':
        try3()
    else:
        try2()
def try3():
    try_to_ext = input("\npress Enter...")
    if try_to_ext == '':
        ext()
    else:
        ext()
if __name__ == '__main__':
    try:
        try:
            main()
        except KeyboardInterrupt:
            print('\nCtrl + C')
            print('\nExiting...')
            sys.exit()
    except EOFError:
        print('\nCtrl + D')
        print('\nExiting...')
        sys.exit()