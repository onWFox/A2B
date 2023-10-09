import shutil
import os

fileName = "DefaultInput.ini"

def makeCopyFile():
    # sas
    
    url = input("Get URL to paste file: ")
    url = url.replace(" ", " ") 

    filePath = os.path.abspath(fileName)
    copyFile =fileName

    shutil.copy2(filePath, url)
    print("END")
