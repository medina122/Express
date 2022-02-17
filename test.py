import os, random
import pyautogui as bot
import pyperclip
from funciones import locate_image
from time import sleep
import re

cclist = []
months = {'01':'1', '02':'2', '03':'3', '04':'4', '05':'5', '06':'6', '07':'7', '08':'8', '09':'9', '10':'10', '11':'11', '12':'12'}
years = {'2022':'1','2023':'2','2024':'3','2025':'4','2026':'5', '2027':'6', '2028':'7', '2029':'8'}
images = {'01':'01', '02':'02', '03':'03', '04':'04','05':'05','06':'06', '07':'07','08':'08','09':'09','10':'10','11':'11','12':'12','22':'22','23':'23','24':'24','25':'25','26':'26','2027':'27', '2028':'28', '2029':'29', '2030':'30', '2031':'31'}

def crear_lista():
    with open('cc.txt', 'r') as file:
        txt_file = file.read().split()

        for line in txt_file:
            card = line.split('|')
            cclist.append(card)

        file.close()

def livear_cc(cc, month, year, cvv):
    
    cc_input = locate_image('credit_card_number', move=False, click=False, output=False) or locate_image('credit_card_number2', move=False, click=False, output=False) 
    month_input = locate_image('exp_month', move=False, click=False, output=False) # or bot.moveTo(cc_input[1][0]+60, cc_input[1][1]+85)
    year_input = locate_image('exp_year', move=False, click=False, output=False) # or bot.moveTo(cc_input[1][0]+190, cc_input[1][1]+85)
    cvv_input = locate_image('cvv', move=False, click=False, output=False) 

    if cc_input: 
            bot.moveTo(cc_input[1][0]+50, cc_input[1][1]+60)
            bot.click()
            sleep(0.10)
            bot.hotkey('ctrl', 'a')
            bot.press('backspace')
            sleep(0.5)
            print(f"CC: {cc}")
            bot.typewrite(cc, interval=0.04)
            sleep(0.20)

    if month_input: 
            bot.moveTo(month_input[1])
            bot.click()
            sleep(1)
            print(f"Month: {month}")
            bot.press('down', int(months[month]), 0.1)
            sleep(0.20)
    else: 
        bot.moveTo(cc_input[1][0]+60, cc_input[1][1]+85)
        bot.click()
        sleep(0.10)
        bot.press('home')
        sleep(1)
        print(f"Month: {month}")
        bot.press('down', int(months[month]), 0.1)
        sleep(0.20)

    if year_input:
            bot.moveTo(year_input[1])
            bot.click()
            sleep(1)
            print(f"Year: {year}")
            bot.press('down', int(years[year]), 0.1)
            sleep(0.20)
    else:
        bot.moveTo(cc_input[1][0]+190, cc_input[1][1]+85)
        bot.click()
        sleep(0.10)
        bot.press('home')
        sleep(1)
        print(f"Year: {year}")
        bot.press('down', int(years[year]), 0.1)
        sleep(0.20)

    if cvv_input:
        bot.moveTo(cvv_input[1][0]+80, cvv_input[1][1]+60)
        bot.click()
        sleep(0.10)
        bot.hotkey('ctrl', 'a')
        bot.press('backspace')
        print(f"Cvv: {cvv}")
        bot.typewrite(cvv, interval=0.05)
        sleep(0.20)

def main():
    crear_lista()
    for cc in cclist:
        livear_cc(cc=cc[0], month=cc[1], year=cc[2], cvv=cc[3])

main()
    
    
    

    
        

