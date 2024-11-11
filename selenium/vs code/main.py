"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Specify the path to chromedriver
service = Service(r"C:/Windows/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://www.nareshit.in/course-schedule/")
time.sleep(5)  # Wait for the page to load

# Locate the first element and click it using JavaScript
element1 = driver.find_element(By.XPATH, "/html/body/div[1]/nav/div/ul/li[5]/a")
driver.execute_script("arguments[0].click();", element1)

time.sleep(5)  # Wait for any potential transitions or page updates

#Locate the second element and click it using JavaScript
element2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/main/article/div/center/a[1]")
driver.execute_script("arguments[0].click();", element2)

time.sleep(5)  # Wait for the action to complete


element3 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/main/article/div/center/a[3]")
driver.execute_script("arguments[0].click();", element3)



