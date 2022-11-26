#--------------------Coded By no1se----------------------#
from selenium import webdriver;
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.select import Select;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium import webdriver
import time;
import colorama;
from colorama import init, Fore, Back, Style;
init()
init(convert=True)
from colorama import Fore, Back, Style;
from pathlib import Path;
from os import system, name;
import os;
from art import *


#---------------------Checking if chromedriver.exe is installed-------------#
chromeexe = Path("C:\Windows\chromedriver.exe")
if chromeexe.is_file():
    print(Back.GREEN + "chromedriver.exe found continuing with the script")
    print(Style.RESET_ALL)
else:
    print(Fore.RED + "Nope I cant find chromedriver.exe please go to here and download https://chromedriver.chromium.org/downloads it move it to windows folder at C")
    quit()
#---------------------Asking questions-----------------------#
print(Fore.WHITE + Back.MAGENTA + "Enter name on catch chat:")
print(Style.RESET_ALL)
catchname = input()
print(Fore.WHITE + Back.MAGENTA + "What is your age gonna be?:")
print(Style.RESET_ALL)
catchage = input()
print(Fore.WHITE + Back.MAGENTA + "What is the message you want to spam?")
print(Style.RESET_ALL)
msg = input()
#------------Next Part get the chromedriver------------------#
ChromeOptions.headless = True
PATH = "C:\Windows\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=PATH)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
#----------------cmd-interface---------------------#
byno1se = "Made By no1se Literally"
print(Back.MAGENTA + Fore.CYAN + """
███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗    ███╗   ██╗ ██████╗  ██╗███████╗███████╗    ██╗     ██╗████████╗███████╗██████╗  █████╗ ██╗     ██╗  ██╗   ██╗██╗██╗██╗
████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝    ████╗  ██║██╔═══██╗███║██╔════╝██╔════╝    ██║     ██║╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║     ██║  ╚██╗ ██╔╝██║██║██║
██╔████╔██║███████║██║  ██║█████╗      ██████╔╝ ╚████╔╝     ██╔██╗ ██║██║   ██║╚██║███████╗█████╗      ██║     ██║   ██║   █████╗  ██████╔╝███████║██║     ██║   ╚████╔╝ ██║██║██║
██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██╗  ╚██╔╝      ██║╚██╗██║██║   ██║ ██║╚════██║██╔══╝      ██║     ██║   ██║   ██╔══╝  ██╔══██╗██╔══██║██║     ██║    ╚██╔╝  ╚═╝╚═╝╚═╝
██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██████╔╝   ██║       ██║ ╚████║╚██████╔╝ ██║███████║███████╗    ███████╗██║   ██║   ███████╗██║  ██║██║  ██║███████╗███████╗██║   ██╗██╗██╗
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝    ╚═╝       ╚═╝  ╚═══╝ ╚═════╝  ╚═╝╚══════╝╚══════╝    ╚══════╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝   ╚═╝╚═╝╚═╝
""")
#----------------Updating Information---------------------#
driver.get("https://catch-chat.com/")
print(driver.title)
tos = driver.find_element("xpath", '//*[@id="pop"]/button')
tos.click()
time.sleep(1)
name = driver.find_element(By.ID, "inpNick")
time.sleep(0.5)
name.send_keys(catchname)
time.sleep(0.5)
age = driver.find_element(By.ID, "inpAge")
time.sleep(0.5)
age.send_keys(catchage)
time.sleep(0.5)
sex = driver.find_element(By.ID, "btnSex")
time.sleep(0.5)
sex.click()
time.sleep(0.5)
catchin = driver.find_element(By.ID, "btnCatchIn")
time.sleep(0.5)
catchin.click()
time.sleep(0.3)
#----------------------loop--------------#
def loop():
    try:
        driver.find_element(By.ID, "toast")
        quit()
    except:
        pass
#----------------------Starting the procces of spam--------------#
for i in msg:
    msgtype = driver.find_element(By.ID, "inpMsg")
    time.sleep(1)
    msgtype.send_keys(msg) #the msg been typed
    time.sleep(0.1)
    msgsent = driver.find_element(By.ID, "btnSend")
    time.sleep(0.1)
    msgsent.click()
    time.sleep(5)
    msgtype.send_keys(i)
driver.quit()
#--------------------Coded By no1se----------------------#