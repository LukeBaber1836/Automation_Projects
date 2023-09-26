from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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


def __main__():
    driver = get_driver("https://automated.pythonanywhere.com/")
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

print(__main__())
