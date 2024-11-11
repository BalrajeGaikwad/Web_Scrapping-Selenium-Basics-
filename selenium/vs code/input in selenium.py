
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to chromedriver
service = Service(r"C:/Windows/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://pwskills.com/")

# Wait for the page to load completely
time.sleep(5)  # Sleep for 5 seconds to ensure the page is fully loaded

# Locate the button and click it
element1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/nav/div/div/div/div[2]/button")
driver.execute_script("arguments[0].click();", element1)

# Additional actions or waiting if needed
time.sleep(5)  # Wait for any page changes after clicking

# Close the driver after the task is done
driver.quit()

