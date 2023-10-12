from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time
import os

s = Service()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service = s, options=chrome_options)
driver.get("https://www.pricecharting.com/category/pokemon-cards")

def run():
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div/div[1]/div[1]/form/button').click()

run()

def getName():
    boo = True
    while (boo):
        name = (driver.find_element(By.CSS_SELECTOR, "a.name").get_attribute("title"))
        if name:
            print(name)
            boo=False
            quit()
            
time.sleep(3)

keyboard = Controller()
keyboard.type("C:\\Users\\jason\\OneDrive\\Desktop\\Scripts\\eBay\\file.png")
keyboard.tap(Key.enter)

time.sleep(15)
driver.implicitly_wait(100)

getName()


