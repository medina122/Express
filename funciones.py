from time import sleep
import pyautogui as bot
import random
import colorama, requests, os, pyperclip
from colorama import Fore

colorama.init()
path = os.getcwd()
tweens = [bot.linear, bot.easeInQuad, bot.easeOutQuad, bot.easeInOutQuad, bot.easeInCubic, bot.easeOutCubic, bot.easeInOutCubic, bot.easeInQuart, bot.easeOutQuart, bot.easeInOutQuart, bot.easeInQuint, bot.easeOutQuint, bot.easeInOutQuint, bot.easeInSine, bot.easeOutSine, bot.easeInOutSine, bot.easeInExpo, bot.easeOutExpo, bot.easeInOutExpo, bot.easeInCirc, bot.easeOutCirc, bot.easeInOutCirc, bot.easeInElastic, bot.easeOutElastic, bot.easeInOutElastic, bot.easeInBack, bot.easeOutBack, bot.easeInOutBack, bot.easeInBounce, bot.easeOutBounce, bot.easeInOutBounce]


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def image_position(img_name: str, conf: float, check: bool):
    image = os.path.join(path, 'src', img_name) + '.png'
    print(image)
    cords = bot.locateOnScreen(image, confidence=conf)

    if cords != (None):
        print(cords)
    elif not cords and check:
        attempt = 0
        sleep(0.25)
        while not cords:
            attempt += 1
            print(f'Locating {img_name}, attempt: {attempt}')
            sleep(0.5)
            cords =  bot.locateOnScreen(image, confidence=conf)
    else: print(f'Not found: {img_name}')    
    return cords
    
def locate_image(img_name, conf=.8, check=False, move=True, click=True, wait=None, end=None):

    if wait != None: sleep(wait)

    image = image_position(img_name, conf, check)

    try:
        if image != (None): 
            if move: bot.moveTo(image, duration=random.randint(10,30)/100, tween=random.choice(tweens))
            if click: 
                bot.click(image, duration=random.randint(10,30)/100, tween=random.choice(tweens))
                # Si le agrego esto, me jodera las variables que usan el movimiento relativo
                # bot.moveRel(random.randint(200,1200), random.randint(100,800))

    except: 
        print('Actions cannot be completed')
    
    if end != None: sleep(end)
    return image


def telegram_report(txt, chatid):
    url = f'https://api.telegram.org/bot1759121577:AAHVHZMjB8cFkxzflzcJbNz1C4vLecxzOrg/sendMessage?chat_id={chatid}&text={txt}'
    requests.post(url)
    print(f"{Fore.GREEN}[Telegram] {Fore.WHITE} Message has been sent! ")
