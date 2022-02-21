import pyautogui as bot
import os
from time import sleep

# Creamos una funcion que se encarge de ubicar imagenes
# recibiendo parametros que activen una opcion u otra

def locate_image(name, co=.8, wait=0, end=0, move=True, click=True, duration=0, check=False, output=True):

    # Ubicamos el CWD y agregamos el folder contenedor de los recursos
    # a utilizar

    image = os.path.join(os.getcwd(), "src", name) + ".png"
        
    # Tiempo muerto antes de iniciar
    if wait != 0: sleep(wait)
    
    # Ubicamos la imagen en la pantalla y establecemos 
    # con la precision por defecto a .8

    cords = bot.locateCenterOnScreen(image, confidence=co)

    # Si el check esta activado, iniciara un bucle hasta que
    # encuentre la imagen en la pantalla

    while check:

        if cords != None:
            break
        else: sleep(0.25)
    
    if cords != None:

        # Confirmacion de que encontro la imagen
        if output: print(f"Image found at {cords}")
    
        # Mover el raton
        if move: bot.moveTo(x=cords[0], y=cords[1], duration=duration)

        # Hacer click con el raton
        if click: bot.click(x=cords[0], y=cords[1])

        # Tiempo muerto al terminar
        if end != 0: sleep(end) 
        return cords, True

    else:
        # Confirmacion de que no encontro la imagen
        if output:
            print(f"Couldn't find image {name}")       
        return False, None

if "__name__" == "__main__":
    locate_image('test', move=False)