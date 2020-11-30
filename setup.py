import os
import requests, zipfile, io

os.system("pip install termcolor")
from termcolor import colored
def getDriver(url, type_of_web):
    path = os.getcwd()+"/data/tools/driver"
    r = requests.get(url, stream=True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(path)
    if type_of_web =="2":
        os.rename(path+ "/geckodriver.exe", path+"/firefoxdriver.exe")
    print(colored("\nGot Driver!\n", "green"))

while True:
    print("""
    0. Quit setup
    1. Google Chrome
    2. Firefox
    """)
    type_of_web = input("Enter your web browser: ")
    if type_of_web == "0":
        break
    elif type_of_web in ("1", "2"):
        try:
            os.stat(os.getcwd()+"/data/tools/driver")
        except:
            os.mkdir(os.getcwd()+"/data/tools/driver")
        try:
            if type_of_web == "1":
                url = "https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_win32.zip"
            elif type_of_web == "2":
                url = "https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-win64.zip"
        except:
            print("something wrong with the website")
        finally:
            getDriver(url, type_of_web)
            set_path = f"set PATH=%PATH%;{os.getcwd()+'/data/tools/driver/driver.exe'}"
            os.system(set_path)
            print(colored("Set path successfully!"))
        break


os.system("pip3 install -r requirements.txt")