
import os
import sys
import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.sberbank.ru/ru/person/credits/homenew'
driver = webdriver.Chrome(os.path.join(sys.path[0], "chromedriver 2"))

def parsing(url=url, driver=driver):

    driver.get(url)

    time.sleep(10)

    info_list = driver.find_elements(By.XPATH, "//div[contains(@class, 'kitt-text kitt-text_size_m product-catalog__description product-catalog__description_desktop')]")
    info_list = [i.text for i in info_list]
    info_list = list(filter(lambda x: x!='',info_list))
    info_list = [re.findall(r'[0-9,]+',i) for i in info_list]

    name_list = [i.text for i in driver.find_elements(By.CSS_SELECTOR, "h2")[:4]]

    dict_par= {}
    for n, name in enumerate(name_list):
        dict_par[name] = info_list[n]

    return dict_par

