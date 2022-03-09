import pyautogui as bot
import os
from time import sleep

cwd = os.getcwd()

def locate(name, co, check=False, move=False, click=False):

    image = os.path.join(cwd, "src", name) + ".png"
    cords = bot.locateCenterOnScreen(image, confidence=co)
    
    if cords: 

        if move:
            bot.moveTo(cords[0], cords[1])

        if click:
            bot.click(cords[0], cords[1])
    
    else:
        print('No pude encontrar la imagen')


        

if __name__ == "__main__":
    # locate_image('windscribe_status_off', check=True)
