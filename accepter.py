#shkipper 

import pyautogui
import time


pictureFound = True
LocationOnPc = 'C:\\Users\\akaki\\Desktop\\Akaki\\PYTHON\\LoLAutoAccepter\\accept.png' #This is different for everyone,
# Just write a path, where you store the uploaded accept.png picture, make sure to use double "\\".  

while (pictureFound) :
    if(pyautogui.locateCenterOnScreen(LocationOnPc)):
        print('found')
        xCor = pyautogui.locateCenterOnScreen(LocationOnPc)[0]
        yCor = pyautogui.locateCenterOnScreen(LocationOnPc)[1]
        print(xCor)
        print(yCor)
        pyautogui.moveTo(xCor,yCor)
        pyautogui.click(xCor,yCor)
        time.sleep(2)
        pictureFound = False
    else:
        time.sleep(3)
        print('not found')
print('program finished')




