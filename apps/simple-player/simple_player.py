from pygame import mixer
import os
import time
import platform
if platform.system() == "Windows":
    clean = "cls"
else:
    clean = "clear"
os.system(clean)
path = os.listdir()
print("---------------------------------------------------")
print("-------------------")
print("Your files:")
print("-------------------")
print(path)
print("---------------------------------------------------")
work = True
file = ""
while(work):
    file = input("Enter file name (exit/pause): ")
    if (file == "pause" or file == "Pause"):
        mixer.music.pause()
        os.system(clean)
        print("---------------------------------------------------")
        print("-------------------")
        print("Your files:")
        print("-------------------")
        print(path)
        print("---------------------------------------------------")
        print("---------------------------------------------------")
        print("Now Playing: " + bfile + " || Paused")
        print("---------------------------------------------------")
        inp = input("Press \"Enter\" to play music")
        os.system(clean)
        mixer.music.unpause()
        print("---------------------------------------------------")
        print("-------------------")
        print("Your files:")
        print("-------------------")
        print(path)
        print("---------------------------------------------------")
        print("---------------------------------------------------")
        print("Now Playing: " + bfile)
        print("---------------------------------------------------")
    elif (file == "exit" or file == "Exit"):
        print("Exiting...")
        work = False
    elif (file != "exit" or file != "pause"):
        bfile = file
        mixer.init()
        time.sleep(0.1)
        print("Loading...")
        mixer.music.load(file)
        time.sleep(0.1)
        print("Done!")
        os.system(clean)
        mixer.music.play()
        print("---------------------------------------------------")
        print("-------------------")
        print("Your files:")
        print("-------------------")
        print(path)
        print("---------------------------------------------------")
        print("---------------------------------------------------")
        print("Now Playing: " + bfile)
        print("---------------------------------------------------")

