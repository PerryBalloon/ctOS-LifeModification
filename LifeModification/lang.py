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