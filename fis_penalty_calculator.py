import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


DATE = "2/26"
EVENT = "SL"
URL = "https://www.skireg.com/Confirmed/6491"
CSV = "FIS-points-list-AL-2023-363.csv"


def get_names(driver):
    first_names = []
    last_names = []

    l = driver.find_elements(By.CLASS_NAME, "day")

    # open each day, get names, then close
    for entry in l:
        if DATE not in entry.text:
            continue

        entry.click() # click to open dropdown and wait until it loads
        WebDriverWait(driver, timeout=10).until(presence_of_element_located((
                      By.CLASS_NAME, "lastname")))

        first_temp = driver.find_elements(By.ID, "tdFirstName")
        last_temp = driver.find_elements(By.CSS_SELECTOR, "td.lastname")
        for first, last in zip(first_temp, last_temp):
            first_names.append(first.text)
            last_names.append(last.text)
        entry.click() # click to close dropdown

    return first_names, last_names


def get_points(first_names, last_names):
    points_list = pd.read_csv(CSV)
    info = points_list[["Lastname", "Firstname", EVENT+"points"]]

    relevant_points = pd.DataFrame()
    for first, last in zip(first_names, last_names):
        new_info = info[(info["Lastname"].str.lower() == last.lower()) & (info["Firstname"].str.lower() == first.lower())]
        new_info = info.loc[(info["Lastname"].str.lower() == last.lower()) & (info["Firstname"].str.lower() == first.lower()), EVENT+"points"]
        relevant_points = pd.concat([relevant_points, new_info])
    
    return relevant_points


# open webpage
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)
driver.maximize_window()
driver.get(URL)

# get necessary info, compute stats
first_names, last_names = get_names(driver)
driver.quit()
event_points = get_points(first_names, last_names)
# MS TODO: calculate the average of the top 5 points, and print out best 10 points

print(event_points)