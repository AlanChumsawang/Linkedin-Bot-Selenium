from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Set username and password as variables or input prompts
username_input = input("Enter your LinkedIn username: ")
password_input = input("Enter your LinkedIn password: ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location="
               "London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)
sign_in_button = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()

username = driver.find_element(By.XPATH, value='//*[@id="username"]')
username.send_keys(username_input)

password = driver.find_element(By.XPATH, value='//*[@id="password"]')
password.send_keys(password_input)

sign_in = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()
time.sleep(5)
jobs = driver.find_elements(By.CSS_SELECTOR, value='.job-card-container--clickable')

for job in jobs:
    try:
        job.click()
        time.sleep(2)
        save_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button")
        save_button.click()
        time.sleep(1)
    except NoSuchElementException:
        pass  # Handle the case where the element is not found

driver.close()
driver.quit()
