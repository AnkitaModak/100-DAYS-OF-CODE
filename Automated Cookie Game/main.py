import threading
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options= chrome_options)
driver.maximize_window()
driver.get("https://cookieclicker.eu/experiments/cookie/")
cookie = driver.find_element(By.XPATH,'//*[@id="cookie"]')
start_time = time.time()
def click_cookie():
    while time.time() - start_time < 300:
        cookie.click()

def buy_upgrades():
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyGrandma"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyFactory"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyMine"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyShipment"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyPortal"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyTime machine"]').click()
        except:
            pass
        time.sleep(5)
threading.Thread(target=click_cookie).start()
threading.Thread(target=buy_upgrades).start()
