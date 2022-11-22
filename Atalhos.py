import keyboard
import os

while True:
    if keyboard.is_pressed("Windows + f10"):
        os.startfile("https://www.youtube.com/")
    if keyboard.is_pressed("Windows + f11"):
        os.startfile("https://www.mercadolivre.com.br/")
    if keyboard.is_pressed("Windows + f12"):
        os.startfile("https://web.whatsapp.com/")
    if keyboard.is_pressed("Windows + f9"):
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    if keyboard.is_pressed("Windows + Z"):
        try:
            os.startfile("C:\CrystalDiskInfo\DiskInfo64.exe")
        except OSError:
            pass
    elif keyboard.is_pressed("tab + esc"):
        break
    
