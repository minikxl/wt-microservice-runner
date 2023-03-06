import os
import shutil
import msvcrt
import subprocess
from time import sleep

MICROSERVICES_DIRS = [
    "Microservice_1",
    "Microservice_2",
    "Microservice_3",
    "Microservice_4",
    "Microservice_FRONTEND_5",
]

PROJECT_NAME = "Project"
DEV_DIR = "Dev"

def run():
    if shutil.which("wt"):
        projDir = ( ".\\" + DEV_DIR if os.path.isdir(DEV_DIR) else ".\\"+ input( "Move script to project folder or enter relative path to project folder: " ))

        for script in MICROSERVICES_DIRS:
            os.system( f' wt --window {PROJECT_NAME} --title {script[:8] if script==MICROSERVICES_DIRS[0] else script[10:]} -d {projDir}\\{script} powershell -noExit ".\mvnw.cmd"' )
            sleep(0.26)

        os.system( f' wt --window {PROJECT_NAME} --title FRONTEND -d {projDir}\\{MICROSERVICES_DIRS[-1]} powershell -noExit "npm start"' )

    else:
        print("Windows Terminal not found \nInstall it and try again: \nhttps://www.microsoft.com/pl-pl/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab" )
        os.system("pause")
        exit()


if __name__ == "__main__":
    print("""
        Menu
        1) Run 
        2) EXIT
    """)
    while True:
        pressedKey = msvcrt.getch()

        if pressedKey == b"1":
            run()
            break
        elif pressedKey in [b"\x1b", b"2"]:
            exit()
