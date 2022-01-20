from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import time


def html_parser(url, delay=0, headless=False, dynamic=True, log_level=0):
    if not dynamic:
        return BeautifulSoup(requests.get(url).text, "html.parser")
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("headless")
    try:
        # silencing log not working
        driver = webdriver.Chrome(ChromeDriverManager(log_level=log_level).install(), options=options)
        driver.get(url)
        time.sleep(delay)
        source = driver.page_source
        driver.quit()
        return BeautifulSoup(source, "html.parser")
    except:
        print("html parser got an error")
        return None


def get_text(target):
    if hasattr(target, "text"):
        return target.text
    try:
        return list(map(get_text, target))
    except:
        return ""