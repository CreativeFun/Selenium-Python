from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
print("sample test case started")

"odpalenie strony selenium"




"""Ustawienie opcji tak, by nie wyświetlał się komunikat o harmness file"""
Options = webdriver.ChromeOptions()
prefs = {'safebrowsing.enabled': 'false'}
Options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev")
driver.maximize_window()

"""Pobranie pliku"""
try:
    driver = webdriver.Chrome(options=Options)
    driver.maximize_window()
    driver.get("https://www.selenium.dev/downloads/")
    gotit = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div/p[1]/a')
    gotit.click()
    #tu powinno być sprawdzenie czy ten plik się pobrał tak naprawdę
except:
    print("Invalid URL")
#zamkniecie przeglądarki
driver.close()
print("sample test case successfully completed")