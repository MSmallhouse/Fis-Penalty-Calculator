# get names of people racing for a given date
from selenium import webdriver
from selenium.webdriver.common.by import By

DATE = "2/27"
URL = "https://www.skireg.com/Confirmed/6491"

first_names = []
last_names = []

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)
driver.maximize_window()
driver.get(URL)
l = driver.find_elements(By.CLASS_NAME, "day")

# open each day, get names, then close
for entry in l:
    if DATE not in entry.text:
        continue

    entry.click()
    first_temp = driver.find_elements(By.ID, "tdFirstName")
    last_temp = driver.find_elements(By.CSS_SELECTOR, "td.lastname")
    for first, last in zip(first_temp, last_temp):
        first_names.append(first.text)
        last_names.append(last.text)
    entry.click()

driver.quit()
