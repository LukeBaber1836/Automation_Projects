from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.chrome.service import Service
import time as t

# Sets options for the browser to make it easier to automate
# Opens site at the given url_value
def get_driver(url_value):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("star-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    browser = webdriver.Chrome(options=options)
    browser.get(url_value)
    
    return browser


def write_to_file(data, write_file):
    current_time = (datetime.now()).strftime("%H:%M:%S")
    write_file.write(current_time + " Temperature value: " + str(data) + "\n")
    

def clean_data(text):
    # Splits text into two elements, [1] gets the number 
    clean_text = float(text.split(": ")[1])
    return clean_text


def scrape(driver):
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]") # scrape data
    return clean_data(element.text)


def login(driver):
    driver.find_element(by="id", value="id_username").send_keys("automated")    # Username input
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)     # Password input
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()   # Click on home
    t.sleep(2)


def __main__():
    driver = get_driver("https://automated.pythonanywhere.com/login/")
    file1 = open("data_scrape_results.txt", "w")
    login(driver) # Login to account

    # Write to the file 10 times
    for i in range(1, 10):
        scraped_val = scrape(driver) # login to website and scape data
        write_to_file(scraped_val, file1) # write new value to file
        t.sleep(2)
    file1.close()
    print("Data collection complete")

# Run program
__main__()
