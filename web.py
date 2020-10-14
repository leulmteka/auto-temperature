import random
import datetime
import selenium
from selenium import webdriver

#opens website on PC
browser = webdriver.Chrome('C:\driver\chromedriver.exe')
browser.get("https://student.risd.org/Identity/Account/Login?ReturnUrl=%2F")
browser.save_screenshot(r'C:\Users\leul\Pictures\selenium-screenshots\image.png') #takes screenshot


#sets chrome to phone instead of PC
options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'com.android.chrome')

browser = webdriver.Chrome('C:\driver\chromedriverphone.exe', chrome_options=options) #opens phone chrome
browser.get('http://seleniumhq.org/')
browser.quit()