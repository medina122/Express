from funciones import locate_image
import pyautogui as bot
import pyperclip, random
from time import sleep

def generar_cc():

    bot.press('win')
    sleep(1)
    bot.typewrite('chrome')
    bot.press('enter')
    sleep(1)
    bot.typewrite('namso-gen.com')
    bot.press('enter')

    locate_image('namso_logo', wait=2, check=True, move=False, click=False)

    if locate_image('namso_bin', end=1)[0]==True:
        bot.typewrite('331534', interval=0.04)
        sleep(0.10)
        bot.press('tab')

    if locate_image('namso_month', end=1)[0]==True:

        for n in range(random.randint(1,9)):
            bot.press('down')

        bot.press('enter')

    if locate_image('namso_year', end=1)[0]==True:

        for n in range(random.randint(1,9)):
            bot.press('down')

        bot.press('enter')

    if locate_image('namso_cvv', end=1)[0]==True:
        bot.typewrite(str(random.randint(000,999)), interval=0.08)

    if locate_image('namso_quantity', end=1)[0]==True:
        bot.typewrite('0')

    locate_image('namso_generate', end=1)
    locate_image('namso_copy', end=1)

    with open('cc.txt', 'w') as file:
        for line in pyperclip.paste():
            if line != '\n':
                file.write(line)
    
    bot.hotkey('ctrl', 'w')

def livear_cc():

    cc = '331534438561472|06|2023|643'
    card = cc.split('|')
    
    creditcard = locate_image('credit_card_number', move=False, click=False) or locate_image('credit_card_number2', move=False, click=False) 
    month = 2

    if creditcard: 
            bot.moveTo(creditcard[1][0]+50, creditcard[1][1]+60)
            bot.click()
            sleep(1)
            bot.typewrite(card[0], interval=0.02)


livear_cc()

            
            


        
    
