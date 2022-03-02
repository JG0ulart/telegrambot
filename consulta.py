import os, inspect, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


#currentdir = os.path.dirname(os.path.abstract(inspect.getfile(inspect.currentframe())))
def verificar_connection(usuario):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--mute-audio')

    browser = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
    browser.set_window_size(1980, 1080)
    browser.get('https://kinney.netwaytelecom.com.br/')

    login_user = browser.find_element_by_xpath('//*[@id="email"]')
    login_user.send_keys('YOU EMAIL LOGIN HERE')

    senha = browser.find_element_by_xpath('//*[@id="password"]')
    senha.send_keys('PASSWORD HERE')

    login_enter = browser.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div/form/button')
    login_enter.click()

    provisio = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[4]/div[1]/ul/li[2]/a')
    provisio.click()

    sleep(3)

    user_consult = browser.find_element_by_xpath('//*[@id="filterInput"]')
    user_consult.click()
    user_consult.send_keys(usuario)

    sleep(5)
    acc_user = browser.find_element_by_xpath('//*[@id="__BVID__21"]/tbody/tr/td[1]/div/a')
    acc_user.click()

    sleep(5)
    status = browser.find_element(By.XPATH, '//*[@id="__BVID__38"]/tbody/tr/td[2]/div').text
    browser.quit()    
    return status

