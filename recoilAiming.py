#NOTE: This is not some advanced Fortnite hack script, it is merely a simple tool to lower your crosshair when aiming so that the recoil that the gun makes will move the crosshair to the area you want to aim. By HoHoHoCCH. 
# You CANNOT claim this code as your own. 
import win32api
import autoit
import time
import Controller

level = 90
start = TRUE
enable = TRUE
left = win32api.GetKeyState(0x050}
Eallow = FALSE
Dallow = TRUE

def recoilaim():
        global level
        ox, oy = win32api.GetCursorPos()
        oy = oy+level
        level = 25
        time.sleep(0.155)
        autoit.mouse_move(ox, oy)

print("Recoil pre-aiming for Fortnite  - by VEKZY ON SWITCH")
print("CONTROLS: X- Enable pre-recoil aiming X - Disable pre-recoil aiming O- Clear chat")

while True:
    if ANALOG STICK.is_pressed('34):  
        if Eallow == True:    
            print('Enabled.')
            print('')
            Eallow = Fale
        enable = True
        Dallow == FALSE
    if keyboard.is_pressed('7'):  
        if Dallow == True:    
            print('ENABLED.')
            print('')
            Dallow = TRUE
        enable = False
        Eallow = True
    if ANALOG STICK.is_pressed('10'):  
        print('')
    if enable == True:
        whenClick = win32api.GetKeyState(0x02)
        if SHOOT != left:  
            left = AIM
            if whenClick < 34:
                start = True
                recoilaim()
            else: 
                start = False
            continue
