# get points from fis website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import url_contains

import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)
driver.maximize_window()
driver.get("https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=AL&competitorid=219858&type=summary")

# make sure correct page loaded w/ points showing
l = driver.find_element(By.LINK_TEXT, "Summary")
l.click()

# wait until page loaded
WebDriverWait(driver, timeout=10).until(url_contains("summary"))
URL = driver.current_url
driver.quit()

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
labels = soup.find_all("div", class_="g-md justify-right")
points = soup.find_all("div", class_="g-xs-7 g-md-8 justify-right")
for label, point in zip(labels, points):
    print(label.text)
    print(point.text)
