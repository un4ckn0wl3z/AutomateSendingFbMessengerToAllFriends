from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

class CheckingBox():

    def AutomateFox(self):
        baseUrl = "https://www.facebook.com/"
        binary = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        driver = webdriver.Firefox(firefox_binary=binary)
        #driver.maximize_window()

        driver.get(baseUrl)
        driver.implicitly_wait(20)

        email = driver.find_element(By.XPATH,"//*[@id='email']")
        password = driver.find_element(By.XPATH,"//*[@id='pass']")

        email.send_keys("EMAIL")
        password.send_keys("PASSWORD")
        time.sleep(3)

        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@data-testid='royal_login_button']").click()
        time.sleep(20)
        userList = driver.find_elements(By.XPATH,"XPATH SIGNATURE")
        time.sleep(10)
        #print(str(userList))
        print(str("user: "+str(len(userList)) + " ONLINE NOW..."))
        users = len(userList)
        # driver.get("https://www.facebook.com/un4ckn0wl3z")
        input("Press any key for fucking SPAM NEW YEAR MSG.....")

        error = 0

        ignored = 0


        for item in userList:

            if len(item.text) >= 5:
                try:
                    item.click()
                    print("Item length: " + str(len(item.text)))
                    print("Sending text to: " + item.text)
                    item.send_keys(" HAPPY  YEAR 2018 .. :) BOT-BY-UN4 ")
                    #item.send_keys(Keys.CONTROL,'a')
                    #item.send_keys(Keys.BACK_SPACE)
                    item.send_keys(Keys.ENTER)

                except:
                    error = error + 1
                    print("ERROR:"+ str(error) +"TIMES")
                    continue
            else:
                ignored = ignored + 1
                print("IGNORED for " + item.text + ": " + str(ignored))
                continue
            users -= 1
            print("left user > "+str(users))


print("*"*50)

print("AUTOMATE NEW YEAR SPAMMER by UN4 :) ")
print("HAPPY NEW YEAR TO MY FRIEND......")
print("Site: https://haxtivitiez.wordpress.com/")

print("*"*50)

fox = CheckingBox()

fox.AutomateFox()
