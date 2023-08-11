import pyautogui
import time
import cv2

while True:
    if pyautogui.locateCenterOnScreen('imf/baby.png', confidence = 0.90, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('imf/baby.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        
    elif pyautogui.locateCenterOnScreen('imf/gae.png', confidence = 0.90, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('imf/gae.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

    elif pyautogui.locateCenterOnScreen('imf/jonna.png', confidence = 0.90, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('imf/jonna.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

    elif pyautogui.locateCenterOnScreen('imf/jot.png', confidence = 0.90, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('imf/jot.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

    elif pyautogui.locateCenterOnScreen('imf/nia.png', confidence = 0.90, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('imf/nia.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

    elif pyautogui.locateCenterOnScreen('imf/niae.png', confidence = 0.90, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('imf/niae.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

    elif pyautogui.locateCenterOnScreen('imf/sibal.png', confidence = 0.90, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('imf/sibal.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

    elif pyautogui.locateCenterOnScreen('imf/sin.png', confidence = 0.90, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('imf/sin.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

    elif pyautogui.locateCenterOnScreen('imf/ssibal.png', confidence = 0.90, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('imf/ssibal.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

    elif pyautogui.locateCenterOnScreen('imf/ziral.png', confidence = 0.90, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('imf/ziral.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

    else:
        pass

