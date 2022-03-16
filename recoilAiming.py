#NOTE: This is not some advanced Fortnite hack script, it is merely a simple tool to lower your crosshair when aiming so that the recoil that the gun makes will move the crosshair to the area you want to aim. By HoHoHoCCH. 
# You CANNOT claim this code as your own. 
import win32api
import autoit
import time
import keyboard

level = 0
start = False
enable = False
left = win32api.GetKeyState(0x01)
Eallow = True
Dallow = False

def recoilaim():
        global level
        ox, oy = win32api.GetCursorPos()
        oy = oy+level
        level = 8
        time.sleep(0.155)
        autoit.mouse_move(ox, oy)

print("Recoil pre-aiming for Fortnite  - by HoHoHoCCH")
print("CONTROLS: \n 6 - Enable pre-recoil aiming \n 7 - Disable pre-recoil aiming \n 8 - Clear chat")

while True:
    if keyboard.is_pressed('6'):  
        if Eallow == True:    
            print('Enabled.')
            print('')
            Eallow = False
        enable = True
        Dallow == True
    if keyboard.is_pressed('7'):  
        if Dallow == True:    
            print('Disabled.')
            print('')
            Dallow = False
        enable = False
        Eallow = True
    if keyboard.is_pressed('8'):  
        print('')
    if enable == True:
        whenClick = win32api.GetKeyState(0x02)
        if whenClick != left:  
            left = whenClick
            if whenClick < 0:
                start = True
                recoilaim()
            else: 
                start = False
            continue
