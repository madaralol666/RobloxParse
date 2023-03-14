import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import lst_link

# Функция прогрузки страницы(самый оптимальный не зависящий от time.sleep())
def wait_load(wait):
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-generic-right-sm"))) # Ждем пока кнопка снизу страницы станет видимой(прогрузиться)

# Функция счета колличества предметов в инвентаре
def count_item(driver, wait):
    wait_load(wait=wait)
    item_elements = driver.find_elements(By.CSS_SELECTOR, "div.item-card-container") # Ищем предметы(Css_selector один их самых быстрых в идеале ID но его нет)
    count_item =+ len(item_elements) # Запись кол-ва предметов.
    return count_item

# Основая функция парсинга инвентаря
def inventory_pars(driver, wait):
    pars_link_account = driver.find_element(By.ID, "nav-inventory").get_attribute("href")
    count_items = 0 # счетчик кол-ва предметов.
    counter = 1 # немного кастыль, счетчик страниц(Page).
    for item_extend_href in lst_link.lst_main_item: # Перебор вкладок инвентаря(lst_link - список содержащий основные(важные) категории предметов).
        pars_href = pars_link_account + '/' + item_extend_href # крафт ссылки для каждой категории.
        driver.get(pars_href) # Обновление ссылки крафт-ссылки.
        count_items += count_item(driver=driver,wait=wait) # Запись кол-ва предметов.
        button_next_page = driver.find_element(By.CSS_SELECTOR, "button.btn-generic-right-sm") # Нахождение кнопки(Page).
        while button_next_page.is_enabled(): # Проверка если доступна для нажатия.
            button_next_page.click()
            if counter % 3 == 0 : time.sleep(1) # Тот самый кастыль, если быстро переключать страницы roblox блокирует каждое 3-е нажатие, поэтому засыпаем на 1 сек.
            count_items += count_item(driver=driver,wait=wait) # Запись кол-ва предметов уже на других страницах(Page)
            counter += 1
    print(count_items)
    driver.quit()
