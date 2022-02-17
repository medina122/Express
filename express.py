import pyautogui as bot
import pyperclip
from funciones import locate_image
from time import sleep
import random

# # PRIMERA PARTE - INICIO / CHECKOUT

# locate_image('express', move=False, click=False, check=True, wait=5, end=2)

# if locate_image('get_future_alerts', move=False, click=False, wait=1, end=1):
#     locate_image('quit_get_alerts')


# locate_image('search', wait=1, end=0.2, check=True)
# locate_image('search2', wait=1, check=True)
# bot.typewrite('Facemask', interval=0.02)
# bot.press('enter', interval=1)
# locate_image('you_searched_for_facemask', duration=0.02, wait=2, end=2, check=True)
# bot.scroll(-(random.randint(190,230)))
# locate_image('facemask', wait=1) or locate_image('facemask2', wait=1)
# locate_image('facemask_title', wait=5, check=True, end=1)
# bot.scroll(-(random.randint(200,250)))
# locate_image('add_to_bag', wait=1, end=2)
# locate_image('item_added', check=True, move=False, click=False)
# locate_image('view_bag', check=True, end=3)
# locate_image('bag_summary', check=True, move=False, click=False)
# sleep(2)
# bot.scroll(-(random.randint(450,550)))
# locate_image('checkout', check=True, wait=2, end=2)
# locate_image('guest_checkout', check=True, wait=2)
# locate_image('checkout_as_guest', check=True, wait=2)

# # # SEGUNDA PARTE - CONTACT INFORMATION
# from generador import nombre, apellido, email, dominio, telefono
# sleep(3)
# locate_image('contact_information', check=True, move=False, click=False)
# bot.typewrite(nombre, interval=0.04)
# bot.press('tab', interval=0.25)
# bot.typewrite(apellido, interval=0.04)
# bot.press('tab', interval=0.25)
# bot.typewrite(email, interval=0.04)
# pyperclip.copy('@')
# bot.hotkey('ctrl', 'v')
# bot.typewrite(dominio, interval=0.04)
# bot.press('tab', interval=0.25)
# bot.typewrite(email, interval=0.04)
# pyperclip.copy('@')
# bot.hotkey('ctrl', 'v')
# bot.typewrite(dominio, interval=0.04)
# bot.press('tab', interval=0.25)
# bot.typewrite(telefono, interval=0.04)
# locate_image('continue', check=True)

# # # TERCERA PARTE - SHIPPING & BILLING ADDRESS

# locate_image('shipping_address', wait=2, end=1, check=True, move=False, click=False)

# bot.press('tab', presses=4, interval=0.2)

# bot.typewrite('1870 NW 82 Av', interval=0.04)
# bot.press('tab')
# bot.typewrite('#'+str(random.randint(00000,99999)), interval=0.04)
# bot.press('tab')
# bot.typewrite('33191', interval=0.04)
# bot.press('tab')
# bot.typewrite('Doral', interval=0.04)
# bot.press('tab')
# bot.press('f')
# bot.scroll(-250)
# locate_image('continue', wait=1.5, end=2)

# locate_image('delivery_options', check=True, move=False, click=False, wait=2)
# locate_image('continue', check=True, wait=1)

# locate_image('payment', check=True, wait=3, move=False, click=False)

creditcard = locate_image('credit_card_number', move=False, click=False) or locate_image('credit_card_number2', move=False, click=False) 

with open('cc.txt', 'r') as file:

    for cc in file.readlines():

        if creditcard: 
            bot.moveTo(creditcard[1][0]+50, creditcard[1][1]+60)
            bot.click()
            sleep(1)
            # bot.typewrite(cc[0], interval=0.02)
            print(cc[0])