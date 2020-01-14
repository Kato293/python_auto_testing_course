from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector ( "button.btn" )
    button.click ()

    confirm = browser.switch_to.alert
    confirm.accept ()

    element = browser.find_element_by_id ( "input_value" )
    x = element.text
    y = calc ( x )

    input1 = browser.find_element_by_id ( "answer" )
    input1.send_keys ( y )

    button = browser.find_element_by_css_selector ( "button.btn" )
    button.click ()
    # добавляем к этому пути имя файла



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
