import os

from makeCopyFile import makeCopyFile

# G:\Epic Games\rocketleague\TAGame\Config


fileName = "DefaultInput.ini"


def getUrl():
    print("|/-\-/-\-/\|")

    url = input("URL to config: ")
    url = url.replace(" ", " ")

    print("-----------")
    print('"' +"The way to file:" + url +'"')
    print("-----------")

    return url


url = getUrl()
url = url+ "\\" + fileName




def removeSoureFile(url):
    try:
        os.remove(url)
        print("The file was successfully deleted (old DefaultInput.ini)")
    except:
        print("No ability to find file. Check your way. Maybe you delete DefaultInput.ini")
        

def Mover():
            removeSoureFile(url)
            makeCopyFile()
            

Mover()