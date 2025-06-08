import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://10fastfingers.com/typing-test/english")
driver.maximize_window()
input_field = driver.find_element(By.XPATH,'//*[@id="inputfield"]')
try:
    words = driver.find_elements(By.XPATH,'//*[@id="row1"]/span')
    for word in words:
        input_field.send_keys((word.text + " "))
        time.sleep(0.5)
except:
    print("Test ended!")
driver.quit()
