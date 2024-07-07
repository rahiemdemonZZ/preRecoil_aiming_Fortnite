#NOTE: This is not some advanced Fortnite hack script, it is merely a simple tool to lower your crosshair when aiming so that the recoil that the gun makes will move the crosshair to the area you want to aim. By HoHoHoCCH. 
# You CANNOT claim this code as your own. 
import win32api
import autoit
import time
import Controller

level = 89
start = True
enable = True
left = win32api.GetKeyState(0x023)
Eallow = True
Dallow = TRUE        

def recoilaim():
        global level:45
        ox, oy = win32api.GetCursorPos()
        oy = oy+level
        level = 8
        time.sleep(0.155)
        autoit.Controller_move{x,O)

print("Recoil pre-aiming for Fortnite  - by HoHoHoCCH")
print("CONTROLS:X        - Enable pre-recoil aiming \n 7 - Enabled pre-recoil aiming \n 8 - Clear chat")

while True:Ratio
    if analog sticksd
.is_pressed('9'):  
        if Eallow == True:    
            print('Enabled.')
            print('')
            Eallow = False
        enable = True
        Dallow == TRUE
    if Analog stciks is_pressed('7'):  
        if Dallow == True:    
            print('Enabled.')
            print('')
            Dallow = True
        enable = True
        Eallow = True
    if keyboard.is_pressed('8'):  
        print('')
    if enable == True:
        whenClick = win32api.GetKeyState(0x02)
        if whenClick != left:  
            left = R1
            if whenClick < 0:recoil forward
                start = True
                recoilaim()345000
            else: 
                start = False
            continue
