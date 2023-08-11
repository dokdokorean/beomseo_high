import pyautogui
import time
import cv2
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import inspect, os, platform, time, random
from datetime import date
import pyperclip

options=webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(executable_path="chromedriver.exe",options=options)

while True:
    if pyautogui.locateCenterOnScreen('lunch/today.png', confidence = 0.99, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('lunch/today.png', confidence = 0.99, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.99, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

        try:
            today = date.today()
            today=str(today)
            today1=today.replace("-","")
            
            driver.get(url='http://school.use.go.kr/beomseo-h/M01030802/list?ymd={}'.format(today1))
            time.sleep(2)
            food=driver.find_element_by_xpath('//*[@id="usm-content-body-id"]/ul[2]/li[1]/dl/dd[1]/ul').text
            pyperclip.copy(food)
            im3 = pyautogui.locateCenterOnScreen('lunch/chat.png', confidence = 0.98, region=(0,0,300, 800))
            pyautogui.click(im3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')
        except:
            pyperclip.copy('중식없음')
            im3 = pyautogui.locateCenterOnScreen('lunch/chat.png', confidence = 0.98, region=(0,0,300, 800))
            pyautogui.click(im3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')
        
    elif pyautogui.locateCenterOnScreen('lunch/today_info.png', confidence = 0.98, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('lunch/today_info.png', confidence = 0.98, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.98, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

        try:
            today = date.today()
            today=str(today)
            today1=today.replace("-","")
            
            driver.get(url='http://school.use.go.kr/beomseo-h/M01030802/list?ymd={}'.format(today1))
            time.sleep(2)
            details= driver.find_element_by_xpath('//*[@id="usm-content-body-id"]/ul[2]/li[4]/dl/dd').text
            pyperclip.copy(details)
            im3 = pyautogui.locateCenterOnScreen('lunch/chat.png', confidence = 0.98, region=(0,0,300, 800))
            pyautogui.click(im3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')
        except:
            pyperclip.copy('중식없음')
            im3 = pyautogui.locateCenterOnScreen('lunch/chat.png', confidence = 0.98, region=(0,0,300, 800))
            pyautogui.click(im3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')

    elif pyautogui.locateCenterOnScreen('lunch/tomorrow.png', confidence = 0.98, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('lunch/tomorrow.png', confidence = 0.98, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.98, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

        try:
            today = date.today()
            today=str(today)
            today1=today.replace("-","")
            today1=int(today1)
            
            driver.get(url='http://school.use.go.kr/beomseo-h/M01030802/list?ymd={}'.format(today1 + 1))
            time.sleep(2)
            food=driver.find_element_by_xpath('//*[@id="usm-content-body-id"]/ul[2]/li[1]/dl/dd[1]/ul').text
            pyperclip.copy(food)
            im3 = pyautogui.locateCenterOnScreen('lunch/chat.png', confidence = 0.98, region=(0,0,300, 800))
            pyautogui.click(im3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')
        except NoSuchElementException:
            pyperclip.copy('내일 중식없음')
            im3 = pyautogui.locateCenterOnScreen('lunch/chat.png', confidence = 0.98, region=(0,0,300, 800))
            pyautogui.click(im3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')

    
    elif pyautogui.locateCenterOnScreen('lunch/tomorrow_info.png', confidence = 0.90, region=(0,0,300, 800)):
        im1 = pyautogui.locateCenterOnScreen('lunch/tomorrow_info.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.rightClick(im1)
        im2 = pyautogui.locateCenterOnScreen('garigi.png', confidence = 0.90, region=(0,0,300, 800))
        pyautogui.moveTo(im2)
        time.sleep(0.2)
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

        try:
            today = date.today()
            today=str(today)
            today1=today.replace("-","")
            today1 = int(today1)
            
            driver.get(url='http://school.use.go.kr/beomseo-h/M01030802/list?ymd={}'.format(today1+1))
            time.sleep(2)
            details= driver.find_element_by_xpath('//*[@id="usm-content-body-id"]/ul[2]/li[4]/dl/dd').text
            pyperclip.copy(details)
            im3 = pyautogui.locateCenterOnScreen('lunch/chat.png', confidence = 0.98, region=(0,0,300, 800))
            pyautogui.click(im3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')
        except:
            pyperclip.copy('내일 중식없음')
            im3 = pyautogui.locateCenterOnScreen('lunch/chat.png', confidence = 0.98, region=(0,0,300, 800))
            pyautogui.click(im3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')

    else:
        pass

