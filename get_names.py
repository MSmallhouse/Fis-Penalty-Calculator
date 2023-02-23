# get names from skireg

# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)
driver.maximize_window()

# launch URL
driver.get("https://www.skireg.com/Confirmed/6491")
# identify element
l = driver.find_elements(By.LINK_TEXT, "+")

# open each day, get names, then close
for button in l:
    button.click()
    first_names = driver.find_elements(By.ID, "tdFirstName")
    last_names = driver.find_elements(By.CSS_SELECTOR, "td.lastname")
    for first, last in zip(first_names, last_names):
        print(f"{first.text} {last.text}")
    button.click()

driver.quit()


#URL = "https://www.skireg.com/Confirmed/6491#"
#page = requests.get(URL)

#soup = BeautifulSoup(page.content, "html.parser")
#first_name = soup.find(class_="event-participant")

# print(soup)