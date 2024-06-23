#OPERATING SYSTEM ctOS _Linux_or_macOS_
import os
import time
from datetime import datetime
import platform
com = str("")
start = "true"
user = "User"
clean = ""
syst = ""
fcheck = open("LifeModification/configs/oobe.cfg", "r")
check = fcheck.read()
fcheck.close()
if(check == "true"):
    if platform.system() == "Windows":
        clean = "cls"
        syst = "| base system: WINDOWS |"
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        clean = "clear"
        syst = "| base system: LINUX   |"                                #основа
    os.system(clean)
    print("╔╗╔╗╔╦═══╦╗  ╔═══╦═══╦═╗╔═╦═══╗")
    print("║║║║║║╔══╣║  ║╔═╗║╔═╗║║╚╝║║╔══╝")
    print("║║║║║║╚══╣║  ║║ ╚╣║ ║║╔╗╔╗║╚══╗")
    print("║╚╝╚╝║╔══╣║ ╔╣║ ╔╣║ ║║║║║║║╔══╝")
    print("╚╗╔╗╔╣╚══╣╚═╝║╚═╝║╚═╝║║║║║║╚══╗")
    print(" ╚╝╚╝╚═══╩═══╩═══╩═══╩╝╚╝╚╩═══╝")
    print("")
    print("Welcome to ctOS: Life Modification")
    print("")
    print("To get started, enter information about yourself:")
    user = open("LifeModification/configs/user.cfg", "w")
    buffer = input("Enter your name: ")
    user.write(buffer + "\n")
    buffer = input("Enter your years old: ")
    user.write(buffer + "\n")
    buffer = input("Enter your city: ")
    user.write(buffer)
    user.close()
    time.sleep(0.3)
    os.system(clean)
    print("Thanks!")
    time.sleep(0.5)
    fcheck = open("LifeModification/configs/oobe.cfg", "w")
    fcheck.write("false")
    fcheck.close()
    time.sleep(1)
    os.system(clean)
    print("╔╗  ╔══╗╔══╗╔═══╗   ╔╗  ╔╗╔══╗╔══╗ ")
    print("║║  ╚╗╔╝║╔═╝║╔══╝   ║║  ║║║╔╗║║╔╗╚╗")
    print("║║   ║║ ║╚═╗║╚══╗   ║╚╗╔╝║║║║║║║╚╗║")
    print("║║   ║║ ║╔═╝║╔══╝   ║╔╗╔╗║║║║║║║ ║║")
    print("║╚═╗╔╝╚╗║║  ║╚══╗   ║║╚╝║║║╚╝║║╚═╝║")
    print("╚══╝╚══╝╚╝  ╚═══╝   ╚╝  ╚╝╚══╝╚═══╝")
    print("Welcome to ctOS: Life Modification!! ^^")
    time.sleep(1)
