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
        syst = "| base system: LINUX   |"                              #основа
    os.system(clean)
    print("╔╗╔╗╔╦═══╦╗  ╔═══╦═══╦═╗╔═╦═══╗")
    print("║║║║║║╔══╣║  ║╔═╗║╔═╗║║╚╝║║╔══╝")
    print("║║║║║║╚══╣║  ║║ ╚╣║ ║║╔╗╔╗║╚══╗")
    print("║╚╝╚╝║╔══╣║ ╔╣║ ╔╣║ ║║║║║║║╔══╝")
    print("╚╗╔╗╔╣╚══╣╚═╝║╚═╝║╚═╝║║║║║║╚══╗")
    print(" ╚╝╚╝╚═══╩═══╩═══╩═══╩╝╚╝╚╩═══╝")
    print("")
    print("Приветствуем тебя в ctOS: Life Modification")
    print("")
    print("Для начала введи информацию о себе:")
    user = open("LifeModification/configs/user.cfg", "w")
    buffer = input("Введи свою имя и фамилию: ")
    user.write(buffer + "\n")
    buffer = input("Введи свой возраст: ")
    user.write(buffer + "\n")
    buffer = input("Введи город проживания: ")
    user.write(buffer)
    user.close()
    time.sleep(0.3)
    os.system(clean)
    print("Спасибо!")
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
    print("Добро пожаловать в ctOS: Life Modification!! ^^")
    time.sleep(1)
