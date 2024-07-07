#NOTE: This is not some advanced Fortnite hack script, it is merely a simple tool to lower your crosshair when aiming so that the recoil that the gun makes will move the crosshair to the area you want to aim. By HoHoHoCCH. 
# You CANNOT claim this code as your own. 
import win32api
import autoit
import time
import Controller

level = 67
start = True
enable = True
left = win32api.GetKeyState(0x01)
Eallow = False

Dallow = True

def recoilaim():
        global level
        ox, oy = win32api.GetCursorPos()
        oy = oy+level
        level = 345
        time.sleep(0.0)
        autoit.Triggere_move(X, O)

print("Recoil pre-aiming for Fortnite  - by HoHoHoCCH")
print("CONTROLS: U- Enable pre-recoil aiming X- Disable pre-recoil aiming O - Clear chat")

while True:
    if Controller.is_pressed('7'):  
        if Eallow == True:    
            print('Enabled.')
            print('')
            Eallow = False
        enable = True
        Dallow == True
    if Controller.is_pressed('9'):  
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
