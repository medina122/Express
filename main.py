import pyautogui as bot
import pyperclip, random
from funciones import locate_image
from time import sleep

cclist = []
months = {'01':'1', '02':'2', '03':'3', '04':'4', '05':'5', '06':'6', '07':'7', '08':'8', '09':'9', '10':'10', '11':'11', '12':'12'}
years = {'2022':'1','2023':'2','2024':'3','2025':'4','2026':'5', '2027':'6', '2028':'7', '2029':'8'}

def preparar_worksplace():
    
    # INICIAMOS EL NAVEGADOR Y ABRIMOS EXPRESS

    bot.press('win')
    sleep(0.25)
    bot.typewrite('Chrome')
    sleep(0.10)
    bot.press('enter')
    sleep(2)
    pyperclip.copy('chrome://settings/clearBrowserData')
    bot.hotkey('ctrl', 'v')
    bot.press('enter')
    locate_image('borrar_datos', check=True)
    sleep(0.10)
    bot.hotkey('ctrl', 'l')
    sleep(0.05)
    bot.typewrite('express.com', interval=0.02)
    bot.press('enter')
    
    # PRIMERA PARTE - INICIO / CHECKOUT

    locate_image('express', move=False, click=False, check=True, wait=5, end=2)

    if locate_image('get_future_alerts', move=False, click=False, wait=1, end=1):
        locate_image('quit_get_alerts')


    locate_image('search', wait=1, end=0.2, check=True)
    locate_image('search2', wait=0.5, check=True)
    bot.typewrite('Facemask', interval=0.02)
    bot.press('enter', interval=1)
    locate_image('express', click=False, check=True)
    locate_image('you_searched_for_facemask', duration=0.01, wait=2, end=5, check=True, click=False, move=False)
    bot.scroll(-(random.randint(190,230)))
    locate_image('facemask', wait=1, end=3) or locate_image('facemask2', wait=1, end=3)
    locate_image('facemask_title', wait=5, check=True, end=1)
    bot.scroll(-(random.randint(200,250)))
    locate_image('add_to_bag', wait=3, end=2)
    locate_image('item_added', check=True, move=False, click=False)
    locate_image('view_bag', check=True, end=3)
    locate_image('bag_summary',wait=3, end=1, check=True, move=False, click=False)
    sleep(2)
    bot.scroll(-(random.randint(450,550)))
    locate_image('checkout', check=True, wait=2, end=2)
    locate_image('guest_checkout', check=True, wait=1, move=False, click=False)
    locate_image('checkout_as_guest', check=True, end=2)

    # # SEGUNDA PARTE - CONTACT INFORMATION
    from generador import nombre, apellido, email, dominio, telefono
    locate_image('contact_information', check=True, move=False, click=False, end=0.2)
    locate_image('first_name', check=True, move=False, click=False, end=0.2)
    bot.typewrite(nombre, interval=0.04)
    bot.press('tab', interval=0.25)
    bot.typewrite(apellido, interval=0.04)
    bot.press('tab', interval=0.25)
    bot.typewrite(email, interval=0.04)
    pyperclip.copy('@')
    bot.hotkey('ctrl', 'v')
    bot.typewrite(dominio, interval=0.04)
    bot.press('tab', interval=0.25)
    bot.typewrite(email, interval=0.04)
    pyperclip.copy('@')
    bot.hotkey('ctrl', 'v')
    bot.typewrite(dominio, interval=0.04)
    bot.press('tab', interval=0.25)
    bot.typewrite(telefono, interval=0.04)
    sleep(0.1)
    locate_image('continue', check=True)

    # # TERCERA PARTE - SHIPPING & BILLING ADDRESS

    locate_image('shipping_address', wait=2, end=1, check=True, move=False, click=False)

    bot.press('tab', presses=3, interval=0.3)

    bot.typewrite('1870 NW 82 Av', interval=0.04)
    bot.press('tab')
    bot.typewrite('#'+str(random.randint(00000,99999)), interval=0.04)
    bot.press('tab')
    bot.typewrite('33191', interval=0.04)
    bot.press('tab')
    bot.typewrite('Doral', interval=0.04)
    bot.press('tab')
    sleep(0.10)
    bot.press('f')
    sleep(0.3)
    bot.scroll(-250)
    locate_image('continue', wait=1.5, end=2)

    locate_image('delivery_options', check=True, move=False, click=False, wait=2)
    locate_image('continue', check=True, wait=1)

    locate_image('payment', check=True, wait=3, move=False, click=False)


def crear_lista():
    with open('cc.txt', 'r') as file:
        txt_file = file.read().split()

        for line in txt_file:
            card = line.split('|')
            cclist.append(card)

        file.close()

def livear_cc(cc, month, year, cvv):
    
    cc_input = locate_image('credit_card_number', move=False, click=False, output=False) or locate_image('credit_card_number2', move=False, click=False, output=False) 
    month_input = locate_image('exp_month', move=False, click=False, output=False)
    year_input = locate_image('exp_year', move=False, click=False, output=False) 
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
    
    locate_image('place_order', wait=1, end=10)

def main():

    preparar_worksplace()
    crear_lista()
    for cc in cclist:
        
        livear_cc(cc=cc[0], month=cc[1], year=cc[2], cvv=cc[3])

        while True:
            
            # if locate_image('place_order', move=False, click=False):
            #     break
            if locate_image('we_experienced_a_problem', move=False, click=False):
                bot.press('f5')
                locate_image('credit_card_number', check=True, move=False, click=False, output=False) 
                break
            elif locate_image('we_are_having_trouble', move=False, click=False):
                break
            elif locate_image('call_us_to_place_order', move=False, click=False):
                bot.hotkey('alt', 'f4')
                preparar_worksplace()
                break
        sleep(0.10)
# main()





    
    
    

    
        

