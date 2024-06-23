#Breadyfetch v3.2 by CyberBr3ad
import os
import platform
import socket
import time
import subprocess, re
from datetime import datetime

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
buffer1 = ""
buffer2 = ""
start = "true"
ver= "0.9" #set by the maintainer
import os

def get_cpu_model_name_windows():
    return os.popen('wmic cpu get name').read().decode()

local_ip=socket.gethostbyname(socket.gethostname())

def get_processor_name():
    if platform.system() == "Windows": #Windows 7 works but other versions im not sure
        vitiacatgay=os.popen('wmic cpu get name').read()
        return vitiacatgay.split("\n")[2]
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command ="sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command).strip()
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).decode().strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub( ".*model name.*:", "",line,1)
    return "idk"

def get_uptime():
    if platform.system()=="Linux":
        return subprocess.check_output("uptime -p", shell=True).decode().strip()
    else:
        return "Only for Linux..."
print("")
print(TextColor.RED + "╔╗  ╔══╗╔══╗╔═══╗   ╔╗  ╔╗╔══╗╔══╗ " + TextColor.RESET, "OS: ctOS", ver, platform.machine())
print(TextColor.RED + "║║  ╚╗╔╝║╔═╝║╔══╝   ║║  ║║║╔╗║║╔╗╚╗" + TextColor.RESET, "Host:", platform.platform())
print(TextColor.GREEN + "║║   ║║ ║╚═╗║╚══╗   ║╚╗╔╝║║║║║║║╚╗║" + TextColor.RESET, "CPU:", get_processor_name())
print(TextColor.GREEN + "║║   ║║ ║╔═╝║╔══╝   ║╔╗╔╗║║║║║║║ ║║" + TextColor.RESET, "Kernel:", platform.version())
print(TextColor.BLUE + "║╚═╗╔╝╚╗║║  ║╚══╗   ║║╚╝║║║╚╝║║╚═╝║" + TextColor.RESET, "Uptime:", get_uptime())
print(TextColor.BLUE + "╚══╝╚══╝╚╝  ╚═══╝   ╚╝  ╚╝╚══╝╚═══╝" + TextColor.RESET, "Local IP:", local_ip)
print("By Aiden Pearce and other developers with love <3")
print("")
