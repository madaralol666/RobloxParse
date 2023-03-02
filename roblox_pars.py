from random import randint
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from progress.bar import IncrementalBar
from colorama import Fore
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
import os
import pickle
import time
import lst_link


# Подмена профиля Firefox + параметры для драйвера
# useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
bar = IncrementalBar('Please, wait!', max = 100)

start_time = time.perf_counter()

useragent = UserAgent().random
service_geck = Service(log_path=os.devnull, executable_path=r'drivers/geckodriver.exe')
options_user = Options()
options_user.set_preference("general.useragent.override", useragent)
options_user.set_preference("javascript.enabled", True)
options_user.add_argument('--headless')
driver = webdriver.Edge(service=service_geck, options=options_user)
driver.get("https://www.roblox.com/Login")

bar.goto(randint(1, 13))
time.sleep(0.3)

def log_in_roblox():

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

bar.goto(randint(14, 26))
time.sleep(0.3)

def dump_cookies():
    # Создаем куки лог/пасса
    pickle.dump(driver.get_cookies(), open(
        f"{lst_link.db_log_pass[0]}_cookies", "wb"))

bar.goto(randint(27, 39))

def login_via_cookies():
    # Вход через куки
    time.sleep(0.2)
    cookies = pickle.load(open(f"{lst_link.db_log_pass[0]}_cookies", "rb"))

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()

bar.goto(randint(40, 50))
time.sleep(0.3)


def inventory_pars():
    # Заход в профиль 
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    robux = soup.find('span', id='nav-robux-amount').text
    href_profile = soup.find('a', class_='text-link dynamic-overflow-container').get('href')
    driver.get(href_profile)

    html_main_profile = driver.page_source
    soup_main_profle = BeautifulSoup(html_main_profile, 'lxml')

    time.sleep(1)
    
    # парсинг данных профиля
    profile_header = soup_main_profle.find('div', class_='profile-header-top')
    display_name = profile_header.find('h1', class_='profile-name text-overflow').text
    friends = profile_header.find_all(class_='font-header-2 ng-binding')[0].text
    followers = profile_header.find_all(class_='font-header-2 ng-binding')[1].text
    following = profile_header.find_all(class_='font-header-2 ng-binding')[2].text
    profile_stat = soup_main_profle.find('p', class_='text-lead').text  # не работает- сделать

    bar.goto(65)
    # Парсинг инвентаря
    soup_inventory = driver.page_source
    bs_soup_inventory = BeautifulSoup(soup_inventory, 'lxml')
    href_Inventory = bs_soup_inventory.find('a', id='nav-inventory').get('href')
    count_item = 0

    for item_extend_href in lst_link.lst_main_item:
        pars_href = href_Inventory + '/' + item_extend_href
        driver.get(pars_href)
        html_item = driver.page_source
        soup_item = BeautifulSoup(html_item, 'lxml')
        # if оптимизации 
        if soup_item.find('div', class_='item-card-container'):
            time.sleep(2.5)
            items = soup_item.find_all('li', class_='list-item item-card ng-scope') 
            count_item += len(items)

            button_check = soup_item.find('button', 'btn-generic-right-sm').get('disabled')

            # Счет страниц
            if button_check is None:

                for page in range(1,100):
                    button_press = driver.find_element(By.CLASS_NAME, 'btn-generic-right-sm')
                    button_press.click()
                    html_item2 = driver.page_source
                    soup_item1 = BeautifulSoup(html_item2, 'lxml')
                    button1_check = soup_item1.find('button', 'btn-generic-right-sm').get('disabled')
                
                    if button1_check != None:
                        time.sleep(1.5)

                    second_item = soup_item1.find_all('li', class_='list-item item-card ng-scope')
                    count_item += len(second_item)
                
                    html_item3 = driver.page_source
                    soup_item2 = BeautifulSoup(html_item3, 'lxml')
                    button2_check = soup_item2.find('button', 'btn-generic-right-sm').get('disabled')

                    if button2_check != None:
                        break 
        else:
            time.sleep(0.2)

        bar.next()

    end_time = time.perf_counter()
    driver.quit
    driver.close
    print( f"\n\n{Fore.RED}In {end_time-start_time:0.2f} seconds")
    
    print( 
        Fore.GREEN + f"\nDisplay Name: {Fore.RESET}{display_name.strip()}" +
        Fore.GREEN + f"\nRobux: {Fore.RESET}{robux}" +
        Fore.GREEN + f"\nFriends: {Fore.RESET}{friends}" +
        Fore.GREEN + f"\nFollowers: {Fore.RESET}{followers}" +
        Fore.GREEN + f"\nFollowing: {Fore.RESET}{following}" +
        Fore.GREEN + f"\nJoin Date: {Fore.RESET}{profile_stat}"+
        Fore.GREEN + f"\nВсего предметов {Fore.RESET}{count_item}"
    )

login_via_cookies()
inventory_pars()
