import time 
import pickle
import lst_link
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def login_via_cookies(driver, wait):
    # Вход через куки
    driver.get('https://www.roblox.com/Login')
    time.sleep(0.2)
    cookies = pickle.load(open(f"{lst_link.db_log_pass[0]}_cookies", "rb"))

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()
    wait.until(EC.url_contains("roblox.com/home"))