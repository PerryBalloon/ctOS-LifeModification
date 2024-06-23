#! LifeModification/configs/system.cfg python
#This is mod by PerryThePlatypus :3
# -*- coding: utf-8 -*-
#OPERATING SYSTEM ctOS
import os
import time
import sys
from datetime import datetime
import platform
import socket
import subprocess, re

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
time.sleep(0.5)    #основа
settings = open("LifeModification/configs/build.cfg", "r")
if (settings == ''):
    settings = 700
build = int(settings.read())
build += 1
settings.close()
set = open("LifeModification/configs/build.cfg", "w")
set.write(str(build))
if(syst == "| base system: LINUX   |"):
    os.system("python3 LifeModification/OS_Loaderpy")
if(syst == "| base system: WINDOWS |"):
    os.system("python LifeModification/OS_Loader.py")
cuser = open("LifeModification/configs/user.cfg", "r")
buffer = cuser.readline()
fix = len(buffer)
user = buffer[:fix-1]
buser = user
buffer3 = cuser.readline()
fix = len(buffer3)
years = buffer3[:fix-1]
city = cuser.readline()
time.sleep(0.1)
os.system(clean)
account = open("LifeModification/configs/.perm.cfg")
activ_key = account.readline()
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
    print(TextColor.CYAN + "||" +TextColor.RESET +" ctOS 0.9 " +TextColor.CYAN + "||" +TextColor.RESET + " в бета тесте       " + TextColor.CYAN + "||" +TextColor.RESET)
    print(TextColor.CYAN + "||" +TextColor.RESET +" Life modification (ver 0.9)    " + TextColor.CYAN + "||" +TextColor.RESET)
    print(TextColor.CYAN + "||" +TextColor.RESET +" Мод сделан: PerryTheBalloon    " + TextColor.CYAN + "||" +TextColor.RESET)
    print(TextColor.CYAN + "||" +TextColor.RESET +" AshotCoins Inc.                " + TextColor.CYAN + "||" +TextColor.RESET)
    print(TextColor.CYAN + "<<================================>>" +TextColor.RESET)
    print("")
    print("Добро пожаловать, " + user + "")
    print("")
    print("Введите 'help' для получения справки")
    print("")
comlog = open("LifeModification/logs/comlog.txt", "w")
buflog = open("LifeModification/logs/buflog.txt", "w")
account = open("LifeModification/configs/.perm.cfg")
if (activ_key != "true"):
    print("Пожалуйста, активируйте ctOS перед использованием")
    login = str(input("Ключ активации: "))
    print("Активация...")
    if(login == activ_key):
        time.sleep(1)
        start = "true"
        os.system(clean)
        account = open("configs/.perm.cfg", "w")
        account.write("true")
        account.close()
        key = 1
    elif(login != activ_key + "\n"):
        time.sleep(1)
        os.system(clean)
        print("Ключ активации неверный.")
        print("Свяжитесь с разработчиком для получения ключа активации")
        print("Нажмите enter для продолжения.")
        input()
        key = 0
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
         print("ACTIVATION")
         print(" ╭──"+ TextColor.GREEN + "["+ user + "@LifeMod]"+ TextColor.RESET + "────"+ TextColor.MAGENTA + "["+ str(time1) +"]" + TextColor.RESET + "────" + TextColor.RED + "["+ str(build) +"]" + TextColor.RESET +"")
         print(TextColor.YELLOW + "["+ str(count) +"]" + TextColor.RESET)
    com = input(" ╰──"+ TextColor.CYAN + "["+ pwd +"]" + TextColor.RESET + "──>>> ")
    buffer = ""
    buffer2 = ""
    comlog.writelines(str(times) + ": " + com + "\n")
    count += 1                                       #Глав. строка
    if (com == 'update'):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/update.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/update.py")
    if (com == 'control'):
        print(TextColor.CYAN + "<<=================>>" + TextColor.RESET)
        print(TextColor.CYAN + "||" + TextColor.RESET + "Панель управления" + TextColor.CYAN + "||" + TextColor.RESET)
        print(TextColor.CYAN + "<<=================>>" + TextColor.RESET)
        print("1. Сменить язык")
        print("2. Действия с пользователями")
        print("3. Обновить/установить модули")
        print("4. Сбросить настройки")
        print("5. О системе")
        buffer = input(TextColor.YELLOW + "Выберите действие: " + TextColor.RESET)
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
            print(TextColor.CYAN + "<<======== Пользователи ========>>" + TextColor.RESET)
            print(TextColor.GREEN + buser +TextColor.RESET)
            print("Admin (Администратор)")
            print(TextColor.RED + "ROOT (Все возможности ОС)" + TextColor.RESET)
            print(TextColor.CYAN + "<<============       ===========>>" + TextColor.RESET)
            print("")
            print("Возможные действия:")
            print("1. Посмотреть информацию о пользователе")
            print("2. Изменить имя пользователя")
            buffer = input(TextColor.YELLOW + "Выберите действие: " + TextColor.RESET)
            if(buffer == "1"):
                print("")
                buffer = input(TextColor.YELLOW + "Введите имя желаемого пользователя: " + TextColor.RESET)
                if (buffer == buser):
                    print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
                    print("Имя: " + user)
                    print(years + " лет")
                    print("Город: " + city)
                    print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
                if (buffer == "ROOT" or buffer == "root" or buffer == "Root" or buffer == "Admin" or buffer == "ADMIN" or buffer == "admin" or buffer == "Administrator"):
                    print("Это системный пользователь.")
            if(buffer == "2"):
                print(TextColor.YELLOW + "Изменене имени пользователя:" + TextColor.RESET)
                print("")
                user = open("LifeModification/configs/user.cfg", "w")
                buffer = input("Введи своё имя: ")
                user.write(buffer + "\n")
                user.close()
                cuser = open("LifeModification/configs/user.cfg", "r")
                buffer = cuser.readline()
                fix = len(buffer)
                user = buffer[:fix-1]
                buser = user
                cuser.close()
                time.sleep(0.3)
                print(TextColor.GREEN + "Готово" + TextColor.RESET)
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
            print("Сброс.")
            time.sleep(0.5)
            os.system(clean)
            print("Сброс..")
            time.sleep(0.5)
            os.system(clean)
            print("Сброс...")
            time.sleep(0.5)
            os.system(clean)
            print("Сброс...Done!")
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
    if (com == "pip"):
        buffer = input("Введите комманду для pip: ")
        if(syst == "| base system: LINUX   |"):
            os.system("python3 -m pip " + buffer)
        if(syst == "| base system: WINDOWS |"):
            os.system("python -m pip " + buffer)
    if(com == "usr edit"):
        print(TextColor.YELLOW + "Изменение информации о себе:" + TextColor.RESET)
        print("")
        user = open("LifeModification/configs/user.cfg", "w")
        buffer = input("Введи своё имя: ")
        user.write(buffer + "\n")
        buffer = input("Введи свой возраст: ")
        user.write(buffer + "\n")
        buffer = input("Введи свой город: ")
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
        print(TextColor.GREEN + "Готово!" + TextColor.RESET)
    if(com == "lang"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 system/lang.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python LifeModification/lang.py")
    if(com == "usr info" or com == "user info"): 
        print("Введите имя пользователя для получения информации: ")
        print("")
        print(TextColor.CYAN + "<<====== Пользователи ======>>" + TextColor.RESET)
        print(TextColor.GREEN + buser + TextColor.RESET)
        print("Administrator (Admin)")
        print(TextColor.RED + "ROOT" + TextColor.RESET)
        print(TextColor.CYAN + "<<======              ======>>" + TextColor.RESET)
        buffer = input("")
        if (buffer == buser):
            print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
            print("Имя: " + user)
            print(years + " лет")
            print("Город: " + city)
            print(TextColor.CYAN + "<<================>>" + TextColor.RESET)
        if (buffer == "ROOT" or buffer == "root" or buffer == "Root" or buffer == "Admin" or buffer == "ADMIN" or buffer == "admin" or buffer == "Administrator"):
            print("Это системный пользователь.")
    if(com == "apt"):
        com = input("Введите команду: ")
        if (com == "install"):
            file_name = input("Введите имя файла для установки пакета: ")
            file = open(file_name, "r", encoding="utf8")
            buffer6 = file.readline(100)
            fix = len(buffer6)
            buffer7 = buffer6[:fix-1]
            buffer5 = file.read()
            print(TextColor.CYAN + "<<==============>>" + TextColor.RESET)
            print("Наименование пакета: " + buffer7)
            print(TextColor.CYAN + "<<==============>>" + TextColor.RESET)
            package = open(buffer7, "w", encoding="utf8")
            package.write(buffer5)
            package.close()
            file.close()
        if(com == "new-package"):       
            file_name = input("Введите имя файла для преобразования в файл установочного пакета: ")
            file = open(file_name, "r")
            buffer1 = file.read()
            backup_name = input("Введите имя файла установочного пакета, но НЕ ИСПОЛЬЗУЙТЕ РАСШИРЕНИЕ ФАЙЛА!!!!!! ")
            backup = open(backup_name + ".ct", "w")
            backup.writelines(file_name + "\n")
            backup.write(buffer1)
            file.close()
            backup.close()
    if(com == "cfile"):
        if(user != "ROOT"):                                             
            print(TextColor.RED + "У вас нет разрешения на эту операцию" + TextColor.RESET)
        if(user == "ROOT"):            
            buffer = input("Введите старый путь к файлу: ")
            buffer2 = input("Введите новый путь к файлу: ")
            os.replace(buffer, buffer2)
    if(com == "fi"):
        if(user == "ROOT"):
            buffer = input("введите название файл (с расширением): ")
            open(buffer, "r")
            print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
            buffer2 = os.stat(buffer)
            print(buffer2)
            print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
            print("st_size — размер файла в байтах")
            print("st_atime — время последнего доступа в секундах (временная метка)")
            print("st_mtime — время последнего изменения")
            print("st_ctime — в Windows это время создания файла, а в Linux — последнего изменения метаданных")
            print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
        if(user != "ROOT"):
            print(TextColor.RED + "У вас нет разрешения на эту операцию" + TextColor.RESET)
    if(com == "df"):
        if(user != "ROOT"):
            print(TextColor.RED + "У вас нет разрешения на эту операцию" + TextColor.RESET)
        if(user == "ROOT"):            
            buffer = input("Введите название файла (с расширением): ")
            os.remove(buffer)
    if(com == "renf"):
        if(user != "ROOT"):
            print(TextColor.RED + "У вас нет разрешения на эту операцию" + TextColor.RESET)
        if(user == "ROOT"):            
            buffer = input("Введите название файла (с расширением): ")
            buffer2 = input("Введите новое название файла (можно с расширением или без) ")
            os.rename(buffer, buffer2)
    if(com == "rf"):
        buffer = input("Введите название файла (с расширением): ")
        file = open(buffer, "r")
        print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
        print(*file)
        print(TextColor.CYAN + "<<====================>>" + TextColor.RESET)
        file.close()
    if(com == "wf"):
        buffer = input("Введите имя файла (с расширением): ")
        file = open(buffer, "w")
        print(TextColor.CYAN + "<<=======================>>" + TextColor.RESET)
        text = input()
        print(TextColor.CYAN + "<<=======================>>" + TextColor.RESET)
        file.write(text)
        time.sleep(0.1)
        file.close()
        print(TextColor.GREEN + "Сохранено!" + TextColor.RESET)
    if(com == "dev"):
        if(user == "ROOT"):
            print(TextColor.CYAN + "<<===================>>" + TextColor.RESET)
            print(TextColor.CYAN + "||" + TextColor.RESET + " ctOS              " + TextColor.CYAN + "||" + TextColor.RESET)
            print(syst)
            print(TextColor.CYAN + "||" + TextColor.RESET + " Build: " + str(build)  + TextColor.CYAN + "        ||" + TextColor.RESET)
            print(TextColor.CYAN + "<<===================>>" + TextColor.RESET)
        if(user != "ROOT"):
            print(TextColor.RED + "У вас нет разрешения на эту операцию" + TextColor.RESET)
    if(com == "cd"):
        buffer = input("Введите НАЗВАНИЕ папки, или оставьте поле пустым, чтобы перейти к корневой папке: ")
        if (buffer != ""):
            os.chdir(buffer)
        if (buffer == ""):
            os.chdir("../")
    if (com == "usr switch" or com == "user switch" or com == "usr change" or com == "user change"):
        print("Select username:")
        print(TextColor.CYAN + "<<========Пользователи========>>" + TextColor.RESET)
        print(TextColor.GREEN + buser +TextColor.RESET)
        print("Admin (Administrator)")
        print(TextColor.RED + "ROOT (Все возможности ОС)" + TextColor.RESET)
        print(TextColor.CYAN + "<<============================>>" + TextColor.RESET)
        print("")
        print(TextColor.YELLOW + "Назад (Введите 'back')" + TextColor.RESET)
        buffer = input()
        if(buffer == "ROOT" or buffer == "root" or buffer == "Root"):
            buffer2 = input(TextColor.YELLOW + "Введите пароль: " + TextColor.RESET)
            if (buffer2 == "5125"):
                user = "ROOT"
                print(TextColor.RED + "<<====================================================>>" +TextColor.RESET)
                print(TextColor.RED + "|| ВНИМАНИЕ! Мы не несем ответственности за все       ||" + TextColor.RESET)
                print(TextColor.RED + "|| Ваши действия в этом пользователе! Будь осторожен! ||" + TextColor.RESET)
                print(TextColor.RED + "<<====================================================>>" +TextColor.RESET)
                time.sleep(0.5)
                print(TextColor.GREEN + "Смена пользователя произошла успешно" + TextColor.RESET)
            if (buffer2 != "5125"):
                print(TextColor.RED + "Неверный пароль!" + TextColor.RESET)
        if(buffer == buser):
            user = buser
            time.sleep(0.5)
            print(TextColor.GREEN + "Смена пользователя произошла успешно" + TextColor.RESET)
    if(com == "ls"):
        if(user != "ROOT"):                                             #Простое разрешение [заметка для разработчика]
            print(TextColor.RED + "У вас нет разрешения на эту операцию" + TextColor.RESET)
        if(user == "ROOT"):
            print(TextColor.CYAN + "<<============       ===========>>" + TextColor.RESET)
            buffer = os.listdir(pwd)
            print(buffer)
            print(TextColor.CYAN + "<<============       ===========>>" + TextColor.RESET)
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
    if (com == "apct"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 LifeModification/apct.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python LifeModification/apct.py")
    if(com == "usr list" or com == "user list" or com == "usr" or com == "users"):
        print("")
        print(TextColor.CYAN + "<<======== Пользователи ========>>" + TextColor.RESET)
        print(TextColor.GREEN + buser +TextColor.RESET)
        print("Admin (Администратор)")
        print(TextColor.RED + "ROOT (Все возможности ОС)" + TextColor.RESET)
        print(TextColor.CYAN + "<<============       ===========>>" + TextColor.RESET)
        print("")
    if(com == "ver"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 LifeModification/vers.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python LifeModification/vers.py")
    if(com == "openpy"):
        buffer = input("Введите путь к файлу или имя файла: ")
        if(syst == "| base system: LINUX   |"):
            os.system("python3 " + buffer)
        if(syst == "| base system: WINDOWS |"):
            os.system("python " + buffer)
    if(com == "run"):
        if(user != "ROOT"):
            print(TextColor.RED + "У вас нет разрешения на эту операцию" + TextColor.RESET)
        if(user == "ROOT"):
            buffer = input("Введите путь к файлу, или имя файла (С РАСШИРЕНИЕМ), или другую команду: ")
            os.system(buffer)
    if(com=="clear"):
        os.system(clean)
    if(com == "md"):
        buffer = input("Введите имя папки: ")
        if not os.path.isdir(buffer):
            os.mkdir(buffer)
            time.sleep(0.05)
            print("Завершено!")
    if(com == "rd"):
        buffer = input("Введите имя папки ")
        os.rmdir(buffer)
        time.sleep(0.05)
        print("Завершено!")
    if(com=="date"):
        print(datetime.today())
    if(com=="help"):
        print(TextColor.CYAN + "<<========                                  ========>>" +TextColor.RESET)
        print("")
        print("Для получения справки введите 'help'")
        print("")
        print(TextColor.CYAN + "<<======== Работа с файами ========>>" +TextColor.RESET)
        print("md - Создать каталог (папку)")
        print("rd - Удалить каталог (папку)")
        print("openpy - Запуск *.py файлов")
        print("rf - Прочитать файл")
        print("cd - переход между папками и каталогами")
        print("apt - install, backup и recover файл или пакет")
        print("wf - Записать информацию в файл или создать новый файл")
        print(TextColor.CYAN + "<<======== Офисные программы ========>>" +TextColor.RESET)
        print("date - Вывод даты и времени")
        print("timer - запуск программы 'таймер'" + TextColor.YELLOW + " [package]" +TextColor.RESET)
        print("calc - калькулятор - Старт калькулятора" + TextColor.YELLOW + " [package]" +TextColor.RESET)
        print("filemgr - файловый менеджер - Запуск файлового менеджера " + TextColor.YELLOW + "[package]" +TextColor.RESET)
        print("calen - Запуск календаря" + TextColor.YELLOW + " [package]" +TextColor.RESET)
        print(TextColor.CYAN + "<<======== Требуется " + TextColor.RED + "ROOT" + TextColor.CYAN + " ========>>" +TextColor.RESET)
        print("ls - Вывод файлов и каталогов " + TextColor.RED + "[ROOT]" +TextColor.RESET)
        print("df - Удалить файл " + TextColor.RED + "[ROOT]" +TextColor.RESET)
        print("renf - Переименовать файл " + TextColor.RED + "[ROOT]"+TextColor.RESET)
        print("fi - Вывод ифнормации о файл " + TextColor.RED + "[ROOT]"+TextColor.RESET)
        print("cfile - Перенос файла " + TextColor.RED + "[ROOT]"+TextColor.RESET)
        print("run - Открытие других файлов " + TextColor.RED + "[ROOT]"+TextColor.RESET)
        print(TextColor.CYAN + "<<======== Параметры ========>>" +TextColor.RESET)
        print("control - открыть панель управления")
        print("lang - Смена языка")
        print("obpy - Установить/обновить модули" + TextColor.YELLOW + " [package]" +TextColor.RESET)
        print("update - обновляет систему до последней версии (не работает на данном кастоме!)")
        print(TextColor.CYAN + "<<======== Работа с пользователями ========>>" +TextColor.RESET)
        print("Примечание: можно писать и usr и user")
        print("usr edit - Изменение информации о пользователе")
        print("usr switch/change - Выбор пользователя")
        print("usr (list) - Вывод всех пользователей в системе и их разрешения")
        print("usr info - вывод информации об опредененном пользователе")
        print(TextColor.CYAN + "========== Другое ========>>" +TextColor.RESET)
        print("echo - Выведите свой текст")
        print("clear - Очистка экрана")
        print("ver - Вывод версии ОС" + TextColor.YELLOW + " [package]" +TextColor.RESET)
        print("clr - Отчистить экран и отобразить приветствие")
        print("pacman - установить (install) новый пакет или создать новый (new-package)")
        print("pip - Ввод комманды для pip")
        print("apct - загрузчик пакетов")
        print(TextColor.CYAN + "<<======== Питание системы ========>>" +TextColor.RESET)
        print("restart - перезагрузка системы")
        print("logout/shutdown/exit - Выключение системы")
        print(TextColor.CYAN + "<<========                                  ========>>" +TextColor.RESET)
    if(com=="clr"): #Does anyone even need this command?
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
           print(TextColor.CYAN + "||" +TextColor.RESET +" ctOS 0.9 " +TextColor.CYAN + "||" +TextColor.RESET + " в бета тесте       " + TextColor.CYAN + "||" +TextColor.RESET)
           print(TextColor.CYAN + "||" +TextColor.RESET +" Life modification (ver 0.9)    " + TextColor.CYAN + "||" +TextColor.RESET)
           print(TextColor.CYAN + "||" +TextColor.RESET +" Мод сделан: PerryTheBalloon    " + TextColor.CYAN + "||" +TextColor.RESET)
           print(TextColor.CYAN + "||" +TextColor.RESET +" AshotCoins Inc.                " + TextColor.CYAN + "||" +TextColor.RESET)
           print(TextColor.CYAN + "<<================================>>" +TextColor.RESET)
           print("")
           print("Добро пожаловать, " + user + "")
           print("")
           print("Введите 'help'для получения помощи")
           print("")
    if(com=="restart"):
        if(syst == "| base system: LINUX   |"):
            os.system(clean)
            print("Перезапуск.")
            time.sleep(0.5)
            os.system(clean)
            print("Перезапуск..")
            time.sleep(0.5)
            os.system(clean)
            print("Перезапуск...")
            time.sleep(0.5)
            os.system(clean)
            print("Перезапуск...Done!")
            time.sleep(0.5)
            start = "false"
            os.system(clean)
            time.sleep(0.1)
            start = "false"
            os.system(clean)
            time.sleep(0.1)
            times1 = datetime.today()
            comlog.writelines("RUS: ")
            comlog.writelines("Перезапуск в: " + str(times1) + "\n")
            os.system("python3 ctOS.py")
        if(syst == "| base system: WINDOWS |"):
            os.system(clean)
            print("Перезапуск.")
            time.sleep(0.5)
            os.system(clean)
            print("Перезапуск..")
            time.sleep(0.5)
            os.system(clean)
            print("Перезапуск...")
            time.sleep(0.5)
            os.system(clean)
            print("Перезапуск...Done!")
            time.sleep(0.5)
            start = "false"
            os.system(clean)
            time.sleep(0.1)
            start = "false"
            os.system(clean)
            time.sleep(0.1)
            times1 = datetime.today()
            comlog.writelines("RUS: ")
            comlog.writelines("Перезапуск в: " + str(times1) + "\n")
            os.system("python ctOS.py")
    if(com==""):
        print("Команда не введена")
    if(com=="obpy"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 LifeModification/ObPy.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python LifeModification/ObPy.py")
    if(com=="calc"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/calcs.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/calcs.py")
    if(com == "echo"):
        buffer = input("Введите текст: ")
        print(buffer)
    if(com=="logout" or com == "exit" or com=="shutdown"):
        os.system(clean)
        print("Завершение работы.")
        time.sleep(0.5)
        os.system(clean)
        print("Завершение работы..")
        time.sleep(0.5)
        os.system(clean)
        print("Завершение работы...")
        time.sleep(0.5)
        os.system(clean)
        print("Завершение работы...Done!")
        time.sleep(0.5)
        start = "false"
        os.system(clean)
        time.sleep(0.1)
        start = "false"
        os.system(clean)
        time.sleep(0.1)
        times1 = datetime.today()
        comlog.writelines("RUS: ")
        comlog.writelines("Завершение работы в: " + str(times1) + "\n")