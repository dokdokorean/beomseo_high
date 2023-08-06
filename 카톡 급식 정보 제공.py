from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import inspect, os, platform, time, random
from datetime import date

options=webdriver.ChromeOptions()
options.add_argument("headless")
current_folder = os.path.realpath( os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
driver_path = os.path.join(current_folder, 'chromedriver')

while True:
    date_input=input()
    if date_input == '오늘 급식' or date_input=='오늘급식':
        try:
            today = date.today()
            today=str(today)
            today1=today.replace("-","")
            
            driver = webdriver.Chrome(driver_path,options=options)
            driver.get(url='http://school.use.go.kr/beomseo-h/M01030802/list?ymd={}'.format(today1))
            time.sleep(2)
            food=driver.find_element_by_xpath('//*[@id="usm-content-body-id"]/ul[2]/li[1]/dl/dd[1]/ul').text
            print(food)

            detail=input()
            
            if detail== '상세' or detail=='오늘 급식 상세' or detail=='급식 상세' or detail=='오늘 상세':
                details= driver.find_element_by_xpath('//*[@id="usm-content-body-id"]/ul[2]/li[4]/dl/dd').text
                print(details)
            else:
                print('한번 더 입력해주세요!')
                
        except:
            print('중식 없음')
            
    elif date_input =='오늘 급식 상세' or date_input=="오늘 급식상세" or date_input=='오늘급식 상세' or date_input=='오늘급식상세':
        try:
            today = date.today()
            today=str(today)
            today1=today.replace("-","")
            
            driver = webdriver.Chrome(driver_path,options=options)
            driver.get(url='http://school.use.go.kr/beomseo-h/M01030802/list?ymd={}'.format(today1))
            time.sleep(2)
            food=driver.find_element_by_xpath('//*[@id="usm-content-body-id"]/ul[2]/li[1]/dl/dd[1]/ul').text
            print(food)
            print('---------------------------------')
            details= driver.find_element_by_xpath('//*[@id="usm-content-body-id"]/ul[2]/li[4]/dl/dd').text
            print(details)
            
        except:
            print('중식 없음')
        
        

    elif date_input=='내일 급식'or date_input=='내일급식':
        try:
            today = date.today()
            today=str(today)
            today1=today.replace("-","")
            today1=int(today1)
            
            driver = webdriver.Chrome(driver_path,options=options)
            driver.get(url='http://school.use.go.kr/beomseo-h/M01030802/list?ymd={}'.format(today1+1))
            time.sleep(2)
            food=driver.find_element_by_xpath('//*[@id="usm-content-body-id"]/ul[2]/li[1]/dl/dd[1]/ul').text
            print(food)
            
            detail=input()
            
            if detail== '상세' or detail=='내일 급식 상세' or detail=='급식 상세':
                details= driver.find_element_by_xpath('//*[@id="usm-content-body-id"]/ul[2]/li[4]/dl/dd').text
                print(details)

            else:
                print('한번 더 입력해주세요')

        except:
            print('중식없음')
            
    elif date_input =='내일 급식 상세' or date_input=="내일 급식상세" or date_input=='내일급식 상세' or date_input=='내일급식상세':
        try:
            today = date.today()
            today=str(today)
            today1=today.replace("-","")
            
            driver = webdriver.Chrome(driver_path,options=options)
            driver.get(url='http://school.use.go.kr/beomseo-h/M01030802/list?ymd={}'.format(today1+1))
            time.sleep(2)
            food=driver.find_element_by_xpath('//*[@id="usm-content-body-id"]/ul[2]/li[1]/dl/dd[1]/ul').text
            print(food)
            print('---------------------------------')
            details= driver.find_element_by_xpath('//*[@id="usm-content-body-id"]/ul[2]/li[4]/dl/dd').text
            print(details)
            
        except:
            print('중식 없음')
    else:
        print('타자가 인식되지 않았습니다. 오타가 있는지 확인해주세요!')
