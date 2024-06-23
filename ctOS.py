import os
import platform
fcheck = open("LifeModification/configs/oobe.cfg", "r")
check = fcheck.read()
fcheck.close()                #base
if platform.system() == "Windows":
    clean = "cls"
    syst = "| base system: WINDOWS |"
elif platform.system() == "Linux":
    clean = "clear"
    syst = "| base system: LINUX   |"                             #основа
lang = open("LifeModification/configs/lang.cfg", "r")
buffer = lang.read()
lg = "rus"
if(buffer == "eng"):
    lg = "eng"
if(buffer == "rus"):
    lg = "rus"
lang.close()
file = open("LifeModification/configs/build.cfg", "w")
file.write("546")
file.close()
if(lg == "eng"):
    if(syst == "| base system: LINUX   |"):
        os.system("python3 LifeModification//EN-en/oobe.py")
        os.system("python3 LifeModification/EN-en/core.py")
    if(syst == "| base system: WINDOWS |"):
        os.system("python LifeModification/EN-en/oobe.py")
        os.system("python LifeModification/EN-en/core.py")
if(lg == "rus"):
    if(syst == "| base system: LINUX   |"):
        os.system("python3 LifeModification/RU-ru/oobe_rus.py")
        os.system("python3 LifeModification/RU-ru/core_ru.py")
    if(syst == "| base system: WINDOWS |"):
        os.system("python LifeModification/RU-ru/oobe_rus.py")
        os.system("python LifeModification/RU-ru/core_ru.py")
        os.system("python LifeModification/RU-ru/logon_ru.py")