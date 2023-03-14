from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import EdgeOptions, Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from progress.bar import IncrementalBar
from colorama import Fore
from fake_useragent import UserAgent
import pickle
import time
import lst_link
import Login_log_pass, Dump_cookie, Login_via_cookie, Inventory_parse

start_time = time.perf_counter()
# Линк на инвентарь игрока, работает только если открыт профиль/или вход по LOG:PASS/или COOCKIE
pars_link_account = "https://www.roblox.com/users/1457973253/inventory"

useragent = UserAgent()
options = EdgeOptions()
# options.add_argument('headless') # Режим без окна + фпсы + скорость
# options.add_argument(useragent.random) # User Agent
options.add_argument('disable-logging') # Отключение не нужных(для смертного) логов
options.add_argument('log-level=3')
driver = Edge(options=options) # Запуск локального вебдрайвера + передача параметров(почему Edge потому что не требует Gdriver, скорость точно такая же)
# driver.get(pars_link_account) # Передачи линки в браузер
wait = WebDriverWait(driver, 10) # Ождание - используется для прогрузки страниц(Page)


# Login_log_pass.log_in_roblox(driver=driver,wait=wait)
# Dump_cookie.dump_cookies(driver=driver)
Login_via_cookie.login_via_cookies(driver=driver, wait=wait)
Inventory_parse.inventory_pars(driver=driver,wait=wait)
end_time = time.perf_counter()
print( f"\n\nIn {end_time-start_time:0.2f} seconds")
