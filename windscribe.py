
from new import locate_image

def change_windscribe_ip():

    locate_image('windscribe_icon', wait=1, end=1.5, output=False)
    
    # locate_image('windscribe_status_on', move=False, click=False, output=False)
    # print('VPN IS ACTIVE - CHANGING IP ADDRESS!')
    # locate_image('windscribe_turn_off')
    # locate_image('windscribe_status_off', check=True, move=False, click=False)
    # locate_image('windscribe_turn_on')
    # locate_image('windscribe_status_on', wait=2, check=True, move=False, click=False)
    # print('done')
    locate_image('windscribe_status_off', move=False, click=False, output=False)
    print('VPN IS OFFLINE, TURNING ON!')
    locate_image('windscribe_turn_on')
    locate_image('windscribe_status_on', wait=2, check=True, move=False, click=False)
    print("Jan")


change_windscribe_ip()
print("12312ASDAS")