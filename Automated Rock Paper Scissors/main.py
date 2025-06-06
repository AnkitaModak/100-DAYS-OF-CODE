import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import tkinter as tk
yesno = input("would you like to play Rock paper Scissors? type y for yes and n for no:").lower()
if yesno == 'y':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://rockpaperscissors-ai.vercel.app/")
    time.sleep(5)
    # 1- Rock
    # 2- Paper
    # 3- Scissor
    your_options = [1,2, 3]
    for _ in range(5):
        move = random.choice(your_options)
        button = driver.find_element(By.XPATH , f'//*[@id="__layout"]/div/div/div[1]/div[3]/div[3]/div[1]/button[{move}]')
        button.click()
        time.sleep(1)
    your_score = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div[1]/div[1]/p[1]').text
    AI_score = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div[1]/div[2]/p[1]').text
    if your_score > AI_score:
        print("CONGGOOOO YOU WONNN!")
    elif AI_score > your_score:
        print("AI wins!Better luck next time!")
    else:
        print("Match Draw!")
    driver.quit()
    yesno = input("would you like to play Rock paper Scissors? type y for yes and n for no").lower()
    if yesno=='n':
        print("Thanks for visiting! Have a Nice day!")
