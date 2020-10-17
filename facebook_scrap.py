from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
import pyperclip
import json
import sys
from datetime import datetime
from tqdm import tqdm
import requests
import re
import os
from download import face_video


usr=input('INGRESA tu  Email de Facebook:')  
pwd=input('INGRESA Password:')  
  
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://www.facebook.com/') 
sleep(1) 
  
username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
sleep(1) 
  
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
  
login_box = driver.find_element_by_xpath("//button[@name='login']") 
login_box.click() 

sleep(3)

driver.get('https://www.facebook.com/watch') 
counter=0
print("INTENTA BAJANDO 20 VECES EL SCROLL\n")
print("ESPERANDO QUE EN ESOS HAYA UN VIDEO DE PUBLICIDAD\n")
while True:
    try:

        menu = driver.find_element_by_xpath('//div[contains(@aria-label, "%s")]' % "Acciones para esta publicaci")
        print("encuentra menu")
        menu.click()
        print("click menu")        

        sleep(5)
        copia_enlace = driver.find_element_by_xpath("//*[contains(text(), 'Copiar enlace')]")
        copia_enlace.click()
        print("copio enlace")
        sleep(1)
        copia=pyperclip.paste()
        print("Intenta descargar el video:")
        print(copia)
        try:
            face_video(copia)
        except:
            print("Facebook no permitio la descarga, pero ahi esta la URL")

        driver.quit()
        sys.exit()
        
    except:
        counter+=1
        if counter<=20:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            print("SCROLL"+ str(counter))
        else:
            print("No encontro publicidad, re intentalo")
            driver.quit()
            sys.exit()
        sleep(10)
