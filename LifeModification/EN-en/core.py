#! configs/system.cfg python
# -*- coding: utf-8 -*-
#OPERATING SYSTEM ctOS
import os
import time
from datetime import datetime
import platform
class TextColor:
    # ANSI escape codes for text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'  # Reset color

com = str("")
start = "false"
user = "User"
clean = ""
syst = ""
buffer = ""
buffer2 = ""
count = 1
security = ""
key = 0
if platform.system() == "Windows":
    clean = "cls"
    syst = "| base system: WINDOWS |"
elif platform.system() == "Linux" or platform.system() == "Darwin":
    clean = "clear"
    syst = "| base system: LINUX   |"      
os.system(clean)   
print("Starting.")
time.sleep(0.3)
os.system(clean)
print("Starting..")
time.sleep(0.3)
os.system(clean)
print("Starting...")
time.sleep(0.5)                #основа
settings = open("LifeModification/configs/build.cfg", "r")
if (settings == ''):
    settings = 700                                #основа
settings = open("LifeModification/configs/build.cfg", "r")
build = int(settings.read())
build += 1
settings.close()
set = open("LifeModification/configs/build.cfg", "w")
set.write(str(build))
if(syst == "| base system: LINUX   |"):
    os.system("python3 LifeModification/OS_Loader.py")
if(syst == "| base system: WINDOWS |"):
    os.system("python LifeModification/OS_Loader.py")
print("ok")
cuser = open("LifeModification/configs/user.cfg", "r")
buffer = cuser.readline()
fix = len(buffer)
user = buffer[:fix-1]
buser = user
buffer3 = cuser.readline()
fix = len(buffer3)
years = buffer3[:fix-1]
city = cuser.readline()
cuser.close()
time.sleep(0.1)
os.system(clean)
comlog = open("LifeModification/logs/comlog.txt", "w")
buflog = open("LifeModification/logs/buflog.txt", "w")
account = open("LifeModification/configs/.perm.cfg")
activ_key = account.readline()
account.close()
print("Choose user, for using this system:")
print(TextColor.CYAN + "<<========    Users   ========>>" + TextColor.RESET)
print(TextColor.GREEN + buser +TextColor.RESET +  " (press Enter)")
print(TextColor.RED + "ROOT (Superuser)" + TextColor.RESET)
print(TextColor.CYAN + "<<============================>>" + TextColor.RESET)
print("")
buffer = input("Username: ")
if(buffer == "ROOT" or buffer == "root" or buffer == "Root"):
    buffer2 = input(TextColor.YELLOW + "Type password: " + TextColor.RESET)
    if (buffer2 == "5125"):
        user = "ROOT"
        print(TextColor.RED + "<<===========================================>>" +TextColor.RESET)
        print(TextColor.RED + "|| ATTENTION! We are not responsible for all ||" + TextColor.RESET)
        print(TextColor.RED + "|| Your actions in this user! Be careful!    ||" + TextColor.RESET)
        print(TextColor.RED + "<<===========================================>>" +TextColor.RESET)
        time.sleep(0.5)
        print(TextColor.GREEN + "Welcome, ROOT!"+ TextColor.RESET)
        time.sleep(1)
        os.system(clean)
    if (buffer2 != "5125"):
        print(TextColor.RED + "Incorrect password! Redirect to non-root user" + TextColor.RESET)
if(buffer == buser or buffer == ""):
        user = buser
        print(TextColor.GREEN + "Welcome, "+ buser +"!"+ TextColor.RESET)
        time.sleep(1)
        os.system(clean)
if (activ_key == "true"):
    print("")
    print(TextColor.RED + "╔╗  ╔══╗╔══╗╔═══╗   ╔╗  ╔╗╔══╗╔══╗ ╔══╗╔══╗╔══╗╔══╗╔══╗╔════╗╔══╗╔══╗╔╗ ╔╗" + TextColor.RESET)
    print(TextColor.RED + "║║  ╚╗╔╝║╔═╝║╔══╝   ║║  ║║║╔╗║║╔╗╚╗╚╗╔╝║╔═╝╚╗╔╝║╔═╝║╔╗║╚═╗╔═╝╚╗╔╝║╔╗║║╚═╝║" + TextColor.RESET)
    print(TextColor.GREEN + "║║   ║║ ║╚═╗║╚══╗   ║╚╗╔╝║║║║║║║╚╗║ ║║ ║╚═╗ ║║ ║║  ║╚╝║  ║║   ║║ ║║║║║╔╗ ║" + TextColor.RESET)
    print(TextColor.GREEN + "║║   ║║ ║╔═╝║╔══╝   ║╔╗╔╗║║║║║║║ ║║ ║║ ║╔═╝ ║║ ║║  ║╔╗║  ║║   ║║ ║║║║║║╚╗║" + TextColor.RESET)
    print(TextColor.BLUE + "║╚═╗╔╝╚╗║║  ║╚══╗   ║║╚╝║║║╚╝║║╚═╝║╔╝╚╗║║  ╔╝╚╗║╚═╗║║║║  ║║  ╔╝╚╗║╚╝║║║ ║║" + TextColor.RESET)
    print(TextColor.BLUE + "╚══╝╚══╝╚╝  ╚═══╝   ╚╝  ╚╝╚══╝╚═══╝╚══╝╚╝  ╚══╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚╝ ╚╝" + TextColor.RESET)
    print("")
    print(TextColor.CYAN + "<<================================>>" +TextColor.RESET)
    print(TextColor.CYAN + "||" +TextColor.RESET +" ctOS 0.9 " +TextColor.CYAN + "||" +TextColor.RESET + " beta test          " + TextColor.CYAN + "||" +TextColor.RESET)
    print(TextColor.CYAN + "||" +TextColor.RESET +" Life modification (ver 0.9)    " + TextColor.CYAN + "||" +TextColor.RESET)
    print(TextColor.CYAN + "||" +TextColor.RESET +" Modified by PerryTheBalloon    " + TextColor.CYAN + "||" +TextColor.RESET)
    print(TextColor.CYAN + "||" +TextColor.RESET +" AshotCoins Inc.                " + TextColor.CYAN + "||" +TextColor.RESET)
    print(TextColor.CYAN + "<<================================>>" +TextColor.RESET)
    print("")
    print("Welcome, " + user + "")
    print("")
    print("Type 'help' for get help")
    print("")
if (activ_key != "true"):
    print("Please activating system before you start using ctOS, or press Enter if not have activation key.")
    login = str(input("Key: ") + "\n")
    print("Activating...")
    if(login == activ_key):
        time.sleep(1)
        start = "true"
        os.system(clean)
        account = open("LifeModification/configs/.perm.cfg", "w")
        account.write("true")
        key = 1
    elif(login != activ_key):
        time.sleep(1)
        os.system(clean)
        key = 0
        print("Key incorrect.")
        print("You using not activated system, please contact at developer for give activation key.")
        input("Press Enter to continue..")
        start = "true"
elif(activ_key == "true"):
    start = "true"
    key = 1
while(start == "true"):
    times = datetime.today()
    if(buffer != ""):
        buflog.writelines(str(times) + " buffer: " + str(buffer) + "\n")
    if(buffer2 != ""):
        buflog.writelines(str(times) + " buffer2: " + str(buffer2) + "\n")
    buffer = ""
    buffer2 = ""
    time1 = datetime.now()
    pwd = os.getcwd()
    if (key == 1):
         print(" ╭──"+ TextColor.GREEN + "["+ user + "@LifeMod]"+ TextColor.RESET + "────"+ TextColor.MAGENTA + "["+ str(time1) +"]" + TextColor.RESET + "────" + TextColor.RED + "["+ str(build) +"]" + TextColor.RESET +"")
         print(TextColor.YELLOW + "["+ str(count) +"]" + TextColor.RESET)
    if (key == 0):
         print("Please activate system.")
         print(" ╭──"+ TextColor.GREEN + "["+ user + "@LifeMod]"+ TextColor.RESET + "────"+ TextColor.MAGENTA + "["+ str(time1) +"]" + TextColor.RESET + "────" + TextColor.RED + "["+ str(build) +"]" + TextColor.RESET +"")
         print(TextColor.YELLOW + "["+ str(count) +"]" + TextColor.RESET)
    com = input(" ╰──"+ TextColor.CYAN + "["+ pwd +"]" + TextColor.RESET + "──>>> ")
    buffer = ""
    buffer2 = ""
    count += 1
    comlog.writelines(str(times) + ": " + com + "\n")   #Глав. строка
    if (com == 'update'):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/update.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/update.py")
    if (com == 'control'):
        print(TextColor.CYAN + "<<=================>>" + TextColor.RESET)
        print(TextColor.CYAN + "||" + TextColor.RESET + "Control panel" + TextColor.CYAN + "||" + TextColor.RESET)
        print(TextColor.CYAN + "<<=================>>" + TextColor.RESET)
        print("1. Change language")
        print("2. Users settings")
        print("3. Install/update modules")
        print("4. Do factory set")
        print("5. About system")
        print("   Or press any key+enter to exit")
        buffer = input(TextColor.YELLOW + "Choose action: " + TextColor.RESET)
        if(buffer == "1"):
            print("")
            print(TextColor.YELLOW + "Хотите сменить язык системы? ")
            print(TextColor.CYAN + "<<================================>>" + TextColor.RESET)
            query = input(TextColor.YELLOW + "Do you want to change the system language?" + TextColor.RESET + " ("+ TextColor.GREEN + "Y" + TextColor.RESET + "/" + TextColor.RED + "n" + TextColor.RESET + ") ")
            print("")
            if(query == "Y" or query == "y"):
                lang = open("LifeModification/configs/lang.cfg", "r")
                buffer = lang.read()
                lg = ""
                if(buffer == "eng"):
                    lg = "eng"
                if(buffer == "rus"):
                    lg = "rus"
                    lang.close()
                langed = open("LifeModification/configs/lang.cfg", "w")
                if(lg == "eng"):
                    langed.write("rus")
                if(lg == "rus"):
                    langed.write("eng")
                    print(TextColor.GREEN + "Язык системы изменён, перезапустите систему для применения параметров." + TextColor.RESET)
                    print(TextColor.CYAN + "<<================================>>" + TextColor.RESET)
                    print(TextColor.GREEN + "The system language has been changed, restart the system to apply the settings." + TextColor.RESET)
            if(query == "n" or query == "N"):
                print(TextColor.YELLOW + "Exiting..." + TextColor.RESET)
        if(buffer == "2"):
            print("")
            print(TextColor.CYAN + "<<======== Users ========>>" + TextColor.RESET)
            print(TextColor.GREEN + buser +TextColor.RESET)
            print("Admin (Administrator)")
            print(TextColor.RED + "ROOT ()" + TextColor.RESET)
            print(TextColor.CYAN + "<<============       ===========>>" + TextColor.RESET)
            print("")
            print("Possible actions:")
            print("1. View user information")
            print("2. Change username")
            print("   Or press any key+enter to exit")
            buffer = input(TextColor.YELLOW + "Select action: " + TextColor.RESET)
            if(buffer == "1"):
                print("")
                buffer = input(TextColor.YELLOW + "Enter the desired username: " + TextColor.RESET)
                if (buffer == buser):
                    print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
                    print("Username: " + user)
                    print(years + " yrs")
                    print("City: " + city)
                    print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
                if (buffer == "ROOT" or buffer == "root" or buffer == "Root" or buffer == "Admin" or buffer == "ADMIN" or buffer == "admin" or buffer == "Administrator"):
                    print("This is a system user.")
            if(buffer == "2"):
                print(TextColor.YELLOW + "Changing username:" + TextColor.RESET)
                print("")
                user = open("LifeModification/configs/user.cfg", "w")
                buffer = input("Enter your username: ")
                user.write(buffer + "\n")
                user.close()
                cuser = open("LifeModification/configs/user.cfg", "r")
                buffer = cuser.readline()
                fix = len(buffer)
                user = buffer[:fix-1]
                buser = user
                cuser.close()
                time.sleep(0.3)
                print(TextColor.GREEN + "Done" + TextColor.RESET)
        if(buffer == "3"):
            if(syst == "| base system: LINUX   |"):
                os.system("python3 LifeModification/ObPy.py")
            if(syst == "| base system: WINDOWS |"):
                os.system("python LifeModification/ObPy.py")
        if(buffer == "4"):
            fcheck = open("LifeModification/configs/oobe.cfg", "w")
            fcheck.write("true")
            fcheck.close()
            user = open("LifeModification/configs/user.cfg", "w")
            user.write("")
            os.system(clean)
            print("Reset.")
            time.sleep(0.5)
            os.system(clean)
            print("Reset..")
            time.sleep(0.5)
            os.system(clean)
            print("Reset...")
            time.sleep(0.5)
            os.system(clean)
            print("Reset...Done!")
            time.sleep(0.5)
            start = "false"
            os.system(clean)
            time.sleep(0.1)
            start = "false"
            os.system(clean)
            time.sleep(0.5)
            os.system("python ctOS.py")
        if(buffer == "5"):
            if(syst == "| base system: LINUX   |"):
                os.system("python3 LifeModification/vers.py")
            if(syst == "| base system: WINDOWS |"):
                os.system("python LifeModification/vers.py")
    if(com == "lang"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 system/lang.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python LifeModification/lang.py")
    if (com == "pip"):
        buffer = input("Enter function for pip: ")
        if(syst == "| base system: LINUX   |"):
            os.system("python3 -m pip " + buffer)
        if(syst == "| base system: WINDOWS |"):
            os.system("python -m pip " + buffer)
    if(com == "usr edit" or com == "user edit"):
        print(TextColor.YELLOW + "User information edit:" + TextColor.RESET)
        print("")
        user = open("LifeModification/configs/user.cfg", "w")
        buffer = input("Enter your username: ")
        user.write(buffer + "\n")
        buffer = input("Enter your years old: ")
        user.write(buffer + "\n")
        buffer = input("Enter your city: ")
        user.write(buffer)
        user.close()
        cuser = open("LifeModification/configs/user.cfg", "r")
        buffer = cuser.readline()
        fix = len(buffer)
        user = buffer[:fix-1]
        buser = user
        buffer3 = cuser.readline()
        fix = len(buffer3)
        years = buffer3[:fix-1]
        city = cuser.readline()
        cuser.close()
        time.sleep(0.3)
        print("")
        print(TextColor.GREEN + "Done!" + TextColor.RESET)
        print("")
    if(com == "usr info" or com == "user info"):
        print("Enter user for print information: ")
        print("")
        print(TextColor.CYAN + "<<======Users======>>" + TextColor.RESET)
        print(TextColor.GREEN + buser + TextColor.RESET)
        print("Administrator (Admin)")
        print(TextColor.RED + "ROOT" + TextColor.RESET)
        print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
        buffer = input("")
        if (buffer == buser):
            print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
            print("Name: " + buser)
            print(years + " years old")
            print("City: " + city)
            print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
        if (buffer == "ROOT" or buffer == "root" or buffer == "Root" or buffer == "Admin" or buffer == "ADMIN" or buffer == "admin" or buffer == "Administrator"):
            print("This is system user.")
    if(com == "pacman"):
        com = input("Enter command: ")
        if (com == "install"):
            file_name = input("Enter file name for install package: ")
            file = open(file_name, "r", encoding="utf8")
            buffer6 = file.readline(100)
            fix = len(buffer6)
            buffer7 = buffer6[:fix-1]
            buffer5 = file.read()
            print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
            print("Package name: " + buffer7)
            print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
            package = open(buffer7, "w", encoding="utf8")
            package.write(buffer5)
            package.close()
            file.close()
        if(com == "new-package"):       
            file_name = input("Enter a file name to convert to an installation package file: ")
            file = open(file_name, "r")
            buffer1 = file.read()
            backup_name = input("Enter the filename of the installation package, but DO NOT USE THE FILE EXTENSION!!!!!! ")
            backup = open(backup_name + ".ct", "w")
            backup.writelines(file_name + "\n")
            backup.write(buffer1)
            file.close()
            backup.close()
    if(com == "cfile"):
        if(user != "ROOT"):                                             
            print(TextColor.RED + "You not have permission for this operation" + TextColor.RESET)
        if(user == "ROOT"):            
            buffer = input("Enter old path file: ")
            buffer2 = input("Enter new path file: ")
            os.replace(buffer, buffer2)
    if(com == "fi"):
        if(user == "ROOT"):
            buffer = input("Enter file: ")
            open(buffer, "r")
            print(TextColor.CYAN + "<<==================>>" + TextColor.RESET)
            buffer2 = os.stat(buffer)
            print(buffer2)
            print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
            print("st_size — file size in bytes")
            print("st_atime — last access time in seconds (timestamp)")
            print("st_mtime — last modified time")
            print("st_ctime — on Windows, this is the time the file was created, and on Linux, the time the metadata was last modified")
            print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
        if(user != "ROOT"):
            print(TextColor.RED + "You not have permission for this operation!" + TextColor.RESET)
    if(com == "df"):
        if(user != "ROOT"):
            print(TextColor.RED + "You not have permission for this operation!" + TextColor.RESET)
        if(user == "ROOT"):            
            buffer = input("Enter file: ")
            os.remove(buffer)
    if(com == "renf"):
        if(user != "ROOT"):
            print(TextColor.RED + "You not have permission for this operation!" + TextColor.RESET)
        if(user == "ROOT"):            
            buffer = input("Enter file: ")
            buffer2 = input("Enter new file name: ")
            os.rename(buffer, buffer2)
    if(com == "rf"):
        buffer = input("Enter file name: ")
        file = open(buffer, "r")
        print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
        print(*file)
        print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
        file.close()
    if(com == "wf"):
        buffer = input("Enter file name: ")
        file = open(buffer, "w")
        print(TextColor.CYAN + "<<=======================>>" + TextColor.RESET)
        text = input()
        print(TextColor.CYAN + "<<=======================>>" + TextColor.RESET)
        file.write(text)
        time.sleep(0.1)
        file.close()
        print(TextColor.GREEN + "Saved!")
    if(com == "dev"):
        if(user == "ROOT"):
            print(TextColor.CYAN + "<<===================>>" + TextColor.RESET)
            print(TextColor.CYAN + "||" + TextColor.RESET + " ctOS              " + TextColor.CYAN + "||" + TextColor.RESET)
            print(syst)
            print(TextColor.CYAN + "||" + TextColor.RESET + " Build: " + str(build)  + TextColor.CYAN + "        ||" + TextColor.RESET)
            print(TextColor.CYAN + "<<===================>>" + TextColor.RESET)
        if(user != "ROOT"):
            print(TextColor.RED + "You not have permission for this operation!" + TextColor.RESET)
    if(com == "cd"):
        buffer = input("Enter the name folder or leave the field blank to go to the root folder: ")
        if (buffer != ""):
            os.chdir(buffer)
        if (buffer == ""):
            os.chdir("../")
    if (com == "usr switch" or com == "user switch" or com == "usr change" or com == "user change"):
        print("Select username:")
        print(TextColor.CYAN + "<<===========Users===========>>" + TextColor.RESET)
        print(TextColor.GREEN + buser +TextColor.RESET)
        print("Admin (Administrator)")
        print(TextColor.RED + "ROOT (All permissions OS)" + TextColor.RESET)
        print(TextColor.CYAN + "<<===========================>>" + TextColor.RESET)
        print("")
        print(TextColor.YELLOW + "Cancel (type 'back')" + TextColor.RESET)
        buffer = input()
        if(buffer == "ROOT" or buffer == "root" or buffer == "Root"):
            buffer2 = input(TextColor.YELLOW + "Enter password: " + TextColor.RESET)
            if (buffer2 == "5125"):
                user = "ROOT"
                print(TextColor.RED + "<<===========================================>>" +TextColor.RESET)
                print(TextColor.RED + "|| ATTENTION! We are not responsible for all ||" + TextColor.RESET)
                print(TextColor.RED + "|| Your actions in this user! Be careful!    ||" + TextColor.RESET)
                print(TextColor.RED + "<<===========================================>>" +TextColor.RESET)
                time.sleep(0.5)
                print(TextColor.GREEN + "Complete" +TextColor.RESET)
                print("")
            if (buffer2 != "5125"):
                print(TextColor.RED + "Password incorrect." +TextColor.RESET)
                print("")
        if(buffer == "Admin" or buffer == "ADMIN" or buffer == "admin"):
            buffer2 = input(TextColor.YELLOW + "Enter password: " +TextColor.RESET)
            if (buffer2 == "0000"):
                user = "Administrator"  
                print(TextColor.GREEN + "Complete" +TextColor.RESET)
            if (buffer2 != "0000"):
                print(TextColor.RED + "Password incorrect." +TextColor.RESET)
        if(buffer == buser):
            user = buser
            time.sleep(0.5)
            print(TextColor.GREEN + "Complete" +TextColor.RESET)
    if(com == "ls"):
        if(user != "ROOT"):                                             #Простое разрешение [заметка для разработчика]
            print(TextColor.RED + "You not have permission for this operation" +TextColor.RESET)
        if(user == "ROOT"):
            print(TextColor.CYAN + "<<========================================>>")
            buffer = os.listdir(pwd)
            print(buffer)
            print(TextColor.CYAN + "<<========================================>>")
    if(com == "timer"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 Programs/timer.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python Programs/timer.py")
    if(com == "usr list"):
        print("")
        print(TextColor.CYAN + "<<===========Users===========>>" + TextColor.RESET)
        print(TextColor.GREEN + buser +TextColor.RESET)
        print("Admin (Administrator)")
        print(TextColor.RED + "ROOT (All permissions OS)" + TextColor.RESET)
        print(TextColor.CYAN + "<<===========================>>" + TextColor.RESET)
        print("")
    if(com=="obpy"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 LifeModification/ObPy.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python LifeModification/ObPy.py")
    if(com == "ver"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 LifeModification/vers.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python LifeModification/vers.py")
    if(com == "timer"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/timer.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/timer.py")
    if(com == "calen"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/Calen.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/Calen.py")
    if(com == "filemgr"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/filemgr.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/filemgr.py")
    if(com == "openpy"):
        buffer = input("Enter the path to the file or file name: ")
        if(syst == "| base system: LINUX   |"):
            os.system("python3 " + buffer)
        if(syst == "| base system: WINDOWS |"):
            os.system(buffer)
    if(com == "run"):
        if(user != "ROOT"):
            print("You not have permission for this operation")
        if(user == "ROOT"):
            buffer = input("Enter the path to the file, or file name, or other command: ")
            os.system(buffer)
    if(com=="clear"):
        os.system(clean)
    if(com == "md"):
        buffer = input("Enter folder name: ")
        if not os.path.isdir(buffer):
            os.mkdir(buffer)
            time.sleep(0.05)
            print("Complete!")
    if(com == "rd"):
        buffer = input("Enter folder name: ")
        os.rmdir(buffer)
        time.sleep(0.05)
        print("Complete!")
    if(com=="date"):
        print(datetime.today())
    if (com == "apct"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 LifeModification/apct.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python LifeModification/apct.py")        
    if(com=="clr"):
        os.system(clean)
        print("")
        print(TextColor.RED + "╔╗  ╔══╗╔══╗╔═══╗   ╔╗  ╔╗╔══╗╔══╗ ╔══╗╔══╗╔══╗╔══╗╔══╗╔════╗╔══╗╔══╗╔╗ ╔╗" + TextColor.RESET)
        print(TextColor.RED + "║║  ╚╗╔╝║╔═╝║╔══╝   ║║  ║║║╔╗║║╔╗╚╗╚╗╔╝║╔═╝╚╗╔╝║╔═╝║╔╗║╚═╗╔═╝╚╗╔╝║╔╗║║╚═╝║" + TextColor.RESET)
        print(TextColor.GREEN + "║║   ║║ ║╚═╗║╚══╗   ║╚╗╔╝║║║║║║║╚╗║ ║║ ║╚═╗ ║║ ║║  ║╚╝║  ║║   ║║ ║║║║║╔╗ ║" + TextColor.RESET)
        print(TextColor.GREEN + "║║   ║║ ║╔═╝║╔══╝   ║╔╗╔╗║║║║║║║ ║║ ║║ ║╔═╝ ║║ ║║  ║╔╗║  ║║   ║║ ║║║║║║╚╗║" + TextColor.RESET)
        print(TextColor.BLUE + "║╚═╗╔╝╚╗║║  ║╚══╗   ║║╚╝║║║╚╝║║╚═╝║╔╝╚╗║║  ╔╝╚╗║╚═╗║║║║  ║║  ╔╝╚╗║╚╝║║║ ║║" + TextColor.RESET)
        print(TextColor.BLUE + "╚══╝╚══╝╚╝  ╚═══╝   ╚╝  ╚╝╚══╝╚═══╝╚══╝╚╝  ╚══╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚╝ ╚╝" + TextColor.RESET)
        print("")
        print(TextColor.CYAN + "<<================================>>" +TextColor.RESET)
        print(TextColor.CYAN + "||" +TextColor.RESET +" ctOS 0.9 " +TextColor.CYAN + "||" +TextColor.RESET + " beta test          " + TextColor.CYAN + "||" +TextColor.RESET)
        print(TextColor.CYAN + "||" +TextColor.RESET +" Life modification (ver 0.9)    " + TextColor.CYAN + "||" +TextColor.RESET)
        print(TextColor.CYAN + "||" +TextColor.RESET +" Modified by PerryTheBalloon    " + TextColor.CYAN + "||" +TextColor.RESET)
        print(TextColor.CYAN + "||" +TextColor.RESET +" AshotCoins Inc.                " + TextColor.CYAN + "||" +TextColor.RESET)
        print(TextColor.CYAN + "<<================================>>" +TextColor.RESET)
        print("")
        print("Welcome, " + user + "")
        print("")
        print("Type 'help' for get help")
        print("")
    if(com=="help"):
         print("")
         print(TextColor.CYAN + "<<========            Help List               ========>>" +TextColor.RESET)
         print("")
         print("For help, type 'help'")
         print("")
         print(TextColor.CYAN + "<<======== Working with files ========>>" +TextColor.RESET)
         print("md - Create directory (folder)")
         print("rd - Delete directory (folder)")
         print("openpy - Run *.py files")
         print("rf - Read file")
         print("cd - switch between folders and directories")
         print("apt - install, backup and recover file or package")
         print("wf - Write information to file or create new file")
         print(TextColor.CYAN + "<<======== Office programs ========>>" +TextColor.RESET)
         print("date - Display date and time")
         print("timer - start program 'timer' " + TextColor.YELLOW + " [package]" +TextColor.RESET)
         print("calc - calculator - Start calculator " + TextColor.YELLOW + " [package]" +TextColor.RESET)
         print("filemgr - file manager - Launching file manager " + TextColor.YELLOW + " [package]" +TextColor.RESET)
         print("calen - Start calendar " + TextColor.YELLOW + " [package]" +TextColor.RESET)
         print(TextColor.CYAN + "<<======== Requires " + TextColor.RED + "ROOT" + TextColor.CYAN + " ========>>" +TextColor.RESET)
         print("ls - List files and directories " + TextColor.RED + "[ROOT]" +TextColor.RESET)
         print("df - Delete file " + TextColor.RED + "[ROOT]" +TextColor.RESET)
         print("renf - Rename file " + TextColor.RED + "[ROOT]" +TextColor.RESET)
         print("fi - Print information about file " + TextColor.RED + "[ROOT]" +TextColor.RESET)
         print("cfile - File transfer " + TextColor.RED + "[ROOT]" +TextColor.RESET)
         print("run - Open other files " + TextColor.RED + "[ROOT]" +TextColor.RESET)
         print(TextColor.CYAN + "<<======== Parameters ========>>" +TextColor.RESET)
         print("control - open control panel")
         print("lang - Change language")
         print("obpy - Install/Upgrade modules")
         print("update - update OS to the lastest version (does not work on this custom!)")
         print(TextColor.CYAN + "<<======== Work with users ========>>" +TextColor.RESET)
         print("Note: you can write both usr and user")
         print("usr edit - Change user information")
         print("usr switch/change - Select user")
         print("usr (list) - Print all users on the system and their permissions")
         print("usr info - print information about a specific user")
         print(TextColor.CYAN + "<<======== Other ========>>" +TextColor.RESET)
         print("echo - Print your text")
         print("clear - Clearing the screen")
         print("ver - Print OS version " + TextColor.YELLOW + " [package]" +TextColor.RESET)
         print("clr - clean screen and display 'Welcome' screen")
         print("pacman - install a new package or create a new one (new-package)")
         print("pip - Enter command for pip")
         print("apct - package downloader")
         print(TextColor.CYAN + "<<======== System Power ========>>" +TextColor.RESET)
         print("restart/reboot - restart OS")
         print("logout/shutdown/exit - Shutdown OS")
         print(TextColor.CYAN + "<<=========                                  ========>>" +TextColor.RESET)
    if(com=="restart" or com=="reboot"):
        if(syst == "| base system: LINUX   |"):
            os.system(clean)
            print("Restarting.")
            time.sleep(0.5)
            os.system(clean)
            print("Restarting..")
            time.sleep(0.5)
            os.system(clean)
            print("Restarting...")
            time.sleep(0.5)
            os.system(clean)
            print("Restarting...Done!")
            time.sleep(0.5)
            start = "false"
            os.system(clean)
            time.sleep(0.1)
            start = "false"
            os.system(clean)
            time.sleep(0.1)
            times1 = datetime.today()
            comlog.writelines("RUS: ")
            comlog.writelines("Restarting in: " + str(times1) + "\n")
            os.system("python3 ctOS.py")
        if(syst == "| base system: WINDOWS |"):
            os.system(clean)
            print("Restart.")
            time.sleep(0.5)
            os.system(clean)
            print("Restart..")
            time.sleep(0.5)
            os.system(clean)
            print("Restart...")
            time.sleep(0.5)
            os.system(clean)
            print("Restart...Done!")
            time.sleep(0.5)
            start = "false"
            os.system(clean)
            time.sleep(0.1)
            start = "false"
            os.system(clean)
            time.sleep(0.1)
            times1 = datetime.today()
            comlog.writelines("RUS: ")
            comlog.writelines("Restarting in: " + str(times1) + "\n")
            os.system("python ctOS.py")
    if(com==""):
        print("Command not typing")
    if(com=="calc"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/calcs.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/calcs.py")
    if(com == "echo"):
        buffer = input("Input string: ")
        print(buffer)
    if(com=="logout" or com == "exit" or com=="shutdown"):
        os.system(clean)
        print("Shutting Down.")
        time.sleep(0.5)
        os.system(clean)
        print("Shutting Down..")
        time.sleep(0.5)
        os.system(clean)
        print("Shutting Down...")
        time.sleep(0.5)
        os.system(clean)
        print("Shutting Down...Done!")
        time.sleep(0.5)
        start = "false"
        os.system(clean)
        time.sleep(0.1)
        start = "false"
        os.system(clean)
        time.sleep(0.1)
        times1 = datetime.today()
        comlog.writelines("ENG: ")
        comlog.writelines("Shutting Down in: " + str(times1) + "\n")