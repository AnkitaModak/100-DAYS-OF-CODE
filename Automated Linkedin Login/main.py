import time
import config
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

your_email = config.email
your_pass = config.password
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.linkedin.com/feed")
time.sleep(5)
email_send= driver.find_element(By.XPATH,'//*[@id="username"]')
email_send.send_keys(your_email, Keys.ENTER)
pass_send = driver.find_element(By.XPATH, '//*[@id="password"]')
pass_send.send_keys(your_pass, Keys.ENTER)
sign_in = driver.find_element(By.XPATH ,'//*[@id="organic-div"]/form/div[4]/button')
sign_in.click()

