import os
import shutil
import getpass
import time

def clearScreen():
    os.system('clear')

clearScreen()

nickname = input("Hi! Welcome to my organizer\nType in your name: ")
username = getpass.getuser()
os.chdir(f"/Users/{username}/Desktop")
def start():
    answ = input("By default your directory that is going to be organized is the desktop, if you wanna change the directory please type in the directory path, OK if you agree the default desktop option or HELP if you are struggling finding how to copy the directory path: ").lower()
    if answ == "ok":
        pass
    elif answ == "help":
        clearScreen()
        print("Press right click on the folder that you want to be organized, click properties and copy the path")
        inp = input("Press any key when done")
        if inp != "":
            pass
        os.chdir(f"{input('Now type the directory path: ')}")
    elif os.path.exists(answ):
        os.chdir(f"{answ}")
    else:
        clearScreen()
        print("Invalid path!Please try again\n")
        start()
    

#print(os.getcwd())
def organize_files():
    clearScreen()
    for num in range(1, 11):
        print('.')
        time.sleep(0.4)
    print("Deleting very old and unused files...")
    time.sleep(1)
    print("Extracting your files...")
    time.sleep(1)
    print("Creating special folders...")
    time.sleep(1.9)
    print("Done!")
    time.sleep(2)
    for file in os.listdir():
        if file == '.DS_Store':
            continue
        name, extension = os.path.splitext(file)
        if extension == "":
            continue
        #print(name, extension)
        extension = extension.replace(".", "")
        if not os.path.exists(f"{nickname} {extension.upper()}'s"):
            os.mkdir(f"{nickname} {extension.upper()}'s")
        shutil.move(file, f"{nickname} {extension.upper()}'s")

def main():
    start()
    organize_files()
    clearScreen()
    if input("Thank you for choosing my program!I hope you are satisfied!\nPress any key to quit") != "":
        quit()
        
main()