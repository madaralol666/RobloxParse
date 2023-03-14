import pickle
import lst_link

def dump_cookies(driver):
    # Создаем куки лог/пасса
    pickle.dump(driver.get_cookies(), open(
        f"{lst_link.db_log_pass[0]}_cookies", "wb"))