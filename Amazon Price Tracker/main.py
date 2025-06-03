import requests
from bs4 import BeautifulSoup
import smtplib
import config
#practice_url ="https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
#to get the header I am using "https://httpbin.org/headers" url
response = requests.get(url=live_url, headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,bn;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
  })
soup = BeautifulSoup(response.text , "html.parser")
price_with_dollar = (soup.find(class_= "aok-offscreen").getText().split()[0])
price = float(price_with_dollar.split("$")[1])
title = soup.find(id="productTitle").getText()
#print(title)
#print(price)
my_email = config.EMAIL_ADDRESS
smtp_email = config.SMTP_ADDRESS
my_pass = config.EMAIL_PASSWORD
if price < 100.00 :
    message = f"{title} is on sale for {price}!"
    connection = smtplib.SMTP(smtp_email , timeout= 60 , port = 587)
    connection.starttls()
    connection.login(user= my_email , password= my_pass)
    connection.sendmail(from_addr=my_email , to_addrs=my_email , msg=f"Subject:Amazon Price Alert!\n\n{message}\n{live_url}".encode("utf-8") )
