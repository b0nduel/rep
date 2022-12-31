from email import message
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import telebot
import os
from selenium.webdriver.common.keys import Keys
import datetime
bot=telebot.TeleBot('5413104861:AAFpYaq7FyBbIe1_OTnIMAxDXOpWu97JVIc')
driver = webdriver.Chrome("C:\chromedriver.exe")  
b=0
c=0

def g1(vin):#вставляет вин и делает скрин капчи
        global driver
        time.sleep(1)
        s=driver.find_element("xpath",'//*[@id="checkAutoVIN"]')
        s.clear
        vin=vin.text
        #f.write(" " + vin)
        s.send_keys(vin)
        driver.find_element("xpath",'//*[@id="checkAutoHistory"]/p[4]').click()
        time.sleep(1)
        driver.get_screenshot_as_file("screenshot.png")
        print(open("screenshot.png","rb"))

def g2(ka):#вставляет капчу,получает и выводит инфу с сайта,нажимает на след кнопку
    try: 
        global driver,b
        b+=1
        driver.find_element(By.NAME,"captcha_num").send_keys(ka.text)
        #driver.find_element("xpath",'//*[@id="captchaSubmit"]').click()
        time.sleep(35)
        h=driver.find_element("xpath",'//*[@id="checkAutoHistory"]/div/ul[2]')
        driver.find_element("xpath",'//*[@id="checkAutoAiusdtp"]/p[3]/a').click()
        time.sleep(2)
        driver.get_screenshot_as_file("screenshot.png")
        return(h.text)
    except:
        b-=1
        driver.find_element("xpath",'//*[@id="checkAutoHistory"]/p[4]').click()
        time.sleep(1)
        driver.get_screenshot_as_file("screenshot.png")
        return("что-то пошло не так отправь код еще раз")

def g4(k):#отправляет 2 капчу и отправляет повреждеия дтп
    try:    
        global driver,b
        b+=1
        driver.find_element(By.NAME,"captcha_num").send_keys(k.text)
        #driver.find_element("xpath",'//*[@id="captchaSubmit"]').click()
        time.sleep(35)
        tet=driver.find_element("xpath",'//*[@id="checkAutoAiusdtp"]/div[1]/ul/li/ul')
        driver.find_element("xpath",'//*[@id="checkAutoWanted"]/p[3]/a').click()
        time.sleep(1)
        driver.get_screenshot_as_file("screenshot.png")
        return(tet.text)
    except:
        b-=1
        driver.find_element("xpath",'//*[@id="checkAutoAiusdtp"]/p[3]/a').click()
        time.sleep(1)
        driver.get_screenshot_as_file("screenshot.png")
        return("что-то пошло не так отправь код еще раз")
def g5(kap1):#розыск
    #try:
        global driver,b
        b+=1
        driver.find_element(By.NAME,"captcha_num").send_keys(kap1.text)
        #driver.find_element("xpath",'//*[@id="captchaSubmit"]').click()
        time.sleep(36)
        te=driver.find_element("xpath",'//*[@id="checkAutoWanted"]/p[2]').text
        if len(str(te)) != len("Проверка CAPTCHA не была пройдена из-за неверного введенного значения."):
            driver.find_element("xpath",'//*[@id="checkAutoRestricted"]/p[3]/a').click()
            time.sleep(1)
            driver.get_screenshot_as_file("screenshot.png")
            return(str(te))
        else:
            b-=1
            driver.find_element("xpath",'//*[@id="checkAutoWanted"]/p[3]/a').click()
            time.sleep(1)
            driver.get_screenshot_as_file("screenshot.png")
            return("что-то пошло не так отправь код еще раз")
def g6(kapc):#ограничения
        global driver,b
        b+=1
        driver.find_element(By.NAME,"captcha_num").send_keys(kapc.text)
        #driver.find_element("xpath",'//*[@id="captchaSubmit"]').click()
        time.sleep(35)
        tex=driver.find_element("xpath",'//*[@id="checkAutoRestricted"]/p[2]').text
        if len(str(tex)) != len("Проверка CAPTCHA не была пройдена из-за неверного введенного значения."):
            driver.find_element("xpath",'//*[@id="checkAutoDiagnostic"]/p[3]/a').click()
            time.sleep(1)
            driver.get_screenshot_as_file("screenshot.png")
            return(tex)
        else:
            b-=1
            driver.find_element("xpath",'//*[@id="checkAutoRestricted"]/p[3]/a').click()
            time.sleep(1)
            driver.get_screenshot_as_file("screenshot.png")
            return("что-то пошло не так отправь код еще раз")
def g7(kapch):
        global driver,b
        b+=1
        driver.find_element(By.NAME,"captcha_num").send_keys(kapch.text)
        #driver.find_element("xpath",'//*[@id="captchaSubmit"]').click()
        time.sleep(35)
        tetx=driver.find_element("xpath",'//*[@id="checkAutoDiagnostic"]/div/ul/li').text
        if len(str(tetx)) != len("Проверка CAPTCHA не была пройдена из-за неверного введенного значения."):
            return(tetx)
        else:
            b-=1
            driver.find_element("xpath",'//*[@id="checkAutoDiagnostic"]/p[3]/a').click()
            time.sleep(1)
            driver.get_screenshot_as_file("screenshot.png")
            return("что-то пошло не так отправь код еще раз")




@bot.message_handler(commands=["start"])
def s(me):
    global driver  
    bot.send_message(me.chat.id,"привет,отправь вин.если ты что-то ввел не правильно,не надо нажимать на все кнопки.бот даст нужные инструкции")
    url="https://xn--90adear.xn--p1ai/check/auto"
    driver.get(url)
    dt = datetime.datetime.now()
    dt_string = dt.strftime("Date: %d/%m/%Y  time: %H:%M:%S")
    f=open("1.txt","a")
    f.write(dt_string)
    f.write(" " + str(me.from_user.username)+"\n")
    f.close() 
    time.sleep(380)

@bot.message_handler(content_types=["text","audio","photo"])
def g(m):
    if m.text.isdigit()==True:
        if b==0:
            t=g2(m)
            bot.send_message(m.chat.id,t)
            photo= open("screenshot.png","rb")
            bot.send_photo(m.chat.id, photo )
        elif b==1:
            bot.send_message(m.chat.id,g4(m))
            bot.send_photo(m.chat.id,open("screenshot.png","rb"))
        elif b==2:
            bot.send_message(m.chat.id,g5(m))
            bot.send_photo(m.chat.id,open("screenshot.png","rb"))
        elif b==3:
            bot.send_message(m.chat.id,g6(m))
            bot.send_photo(m.chat.id,open("screenshot.png","rb"))
        elif b==4:
            bot.send_message(m.chat.id,g7(m))
            if b==5:
                bot.send_photo(m.chat.id,open("s.jpg","rb"))
            elif b==4:        
                bot.send_photo(m.chat.id,open("screenshot.png","rb"))
    else:
        g1(m)
        photo= open("screenshot.png","rb")
        bot.send_photo(m.chat.id, photo )
              


bot.polling(none_stop=True)
