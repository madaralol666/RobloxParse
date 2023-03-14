from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import lst_link
def log_in_roblox(driver,wait):

    # ссылка сайта
    driver.get("https://www.roblox.com/Login")

    # Ввод логина
    email_input = driver.find_element(By.ID, 'login-username')
    email_input.click()
    email_input.clear()
    email_input.send_keys(lst_link.db_log_pass[0])
    email_input.send_keys(Keys.ENTER)

    # Ввод пароля
    pass_input = driver.find_element(By.ID, 'login-password')
    pass_input.click()
    pass_input.clear()
    pass_input.send_keys(lst_link.db_log_pass[1])
    pass_input.send_keys(Keys.ENTER)

    wait.until(EC.url_contains("roblox.com/home"))

    inventory_button = driver.find_element(By.ID, 'nav-inventory')
    inventory_button.click()