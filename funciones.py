from time import sleep
import pyautogui as bot
import random
import colorama, requests, os, pyperclip
from colorama import Fore

colorama.init()

tweens = [bot.linear, bot.easeInQuad, bot.easeOutQuad, bot.easeInOutQuad, bot.easeInCubic, bot.easeOutCubic, bot.easeInOutCubic, bot.easeInQuart, bot.easeOutQuart, bot.easeInOutQuart, bot.easeInQuint, bot.easeOutQuint, bot.easeInOutQuint, bot.easeInSine, bot.easeOutSine, bot.easeInOutSine, bot.easeInExpo, bot.easeOutExpo, bot.easeInOutExpo, bot.easeInCirc, bot.easeOutCirc, bot.easeInOutCirc, bot.easeInElastic, bot.easeOutElastic, bot.easeInOutElastic, bot.easeInBack, bot.easeOutBack, bot.easeInOutBack, bot.easeInBounce, bot.easeOutBounce, bot.easeInOutBounce]


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def locate(name, move=True, click=True, co=0.8, wait=0, end=0, duration=random.randint(10,25)/100, output=True):

    if wait != 0: sleep(wait)

    path = os.path.abspath(os.path.dirname(__file__))
    data = ''

    if path.startswith('C:'):
        data = path +f'\src\{name}.png'
    
    else:
        data = path +f'/src/{name}.png'

    global cords
    cords = bot.locateOnScreen(data, confidence=co)

    if cords:

        if move:
            bot.moveTo(cords, tween=random.choice(tweens), duration=duration)

        if click:
            bot.click(cords, duration=duration)

        if output:
            print(f'Found {name} at {cords[0], cords[1]}')

        if end != 0: sleep(end)

        return True, cords
        
    else: 
        if output:
            print(f'Not found {name}')
        return False, None

def locate_image(name, move=True, click=True, co=0.8, wait=0, end=0, duration=0.20, output=True, check=False):

    if check:

        if wait != 0:
            sleep(wait)

        while True:

            sleep(0.25)
            if locate(name, move, click, co, duration, output)[0] == True:
                break
            else: sleep(1)
        
        if end != 0: sleep(end)
        return True, cords
    
    else:
        if locate(name, move, click, co, wait, end, duration, output)[0]==True:
            return True, cords


def telegram_report(txt, chatid):
    url = f'https://api.telegram.org/bot1759121577:AAHVHZMjB8cFkxzflzcJbNz1C4vLecxzOrg/sendMessage?chat_id={chatid}&text={txt}'
    requests.post(url)
    print(f"{Fore.GREEN}[Telegram] {Fore.WHITE} Message has been sent! ")
