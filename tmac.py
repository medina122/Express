from new import locate_image

def change_mac():
    locate_image('tmac_icon', wait=1, end=1)
    locate_image('tmac_ethernet', end=1)
    locate_image('tmac_random', end=1)
    locate_image('tmac_change', end=1)
    locate_image('tmac_mac_changed', move=False, click=False, wait=1, check=True)
    locate_image('tmac_aceptar')

    print('Mac has been changed!')

change_mac()
print('Finished')