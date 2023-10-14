from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

def run():
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div/div[1]/div[1]/form/button').click()

def getName():
    boo = True
    driver.implicitly_wait(200)
    while (boo):
        print("here")
        name = (driver.find_element(By.CSS_SELECTOR, "a.name").get_attribute("title"))
        if name:
            print(name)
            boo=False
            quit()

s = Service()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service = s, options=chrome_options)
driver.get("https://www.pricecharting.com/category/pokemon-cards")

run()

time.sleep(3)

keyboard = Controller()
keyboard.type("C:\\Users\\jason\\OneDrive\\Desktop\\Scripts\\eBay\\file.png")
keyboard.tap(Key.enter)

getName()


