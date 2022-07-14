"""
Kacper Konwerski zadanie rekrutacyjne 14.07.2022
środowisko na którym zostało wykonane win10
używając servera chrominium (/103.0.5060.53/chromedriver_win32.zip)
opis zadania w swpraca.txt
"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""ustawienie dodatkowych opcji na pominięcie komunikatu harmness file (z drugiej strony można by to dać w metodę download ale wtedy by należało robić nowego drivera
a zależało w sumie mi na ciągłości okna bo ładniej wygląda)"""

Options = webdriver.ChromeOptions()
prefs = {'safebrowsing.enabled': 'false'}
Options.add_experimental_option("prefs", prefs)

#stałe z linkami do stron oraz czasami
selenium_main = "https://www.selenium.dev"
selenium_downloads = "https://www.selenium.dev/downloads/"
loading_time = 5
truesecond = 1
driver = webdriver.Chrome(options=Options)

def constant_wait():
    constant_wait = 3
    for i in range(constant_wait):
        print("Waiting for site to fully load, time left {} (s)".format(constant_wait - i))
        time.sleep(truesecond)
    print("PASS")
    return time.sleep(constant_wait)

def pageopen(url):
    print("Trying to get {}".format(url))
    try:
        driver.get(url)
        driver.maximize_window()
        print("Waiting {} s to load the site".format(loading_time))
        for i in range(loading_time):
            print("Time left {}".format(loading_time - i))
            time.sleep(truesecond)
        print("PASS")
    except Exception as e:
        print("FAIL")
        print(e.message)
        driver.close()

def searchphrase():
    string = "XDDDDDD"
    try:
        searchbar = driver.find_element(By.ID, 'docsearch')
        searchbar.click()
        constant_wait()
        try:
            text = driver.find_element(By.ID, 'docsearch-input')
            text.click()
            text.send_keys(string)
            text.send_keys(Keys.ENTER)
            constant_wait()
        except Exception as e:
            print("FAIL")
            print(e.message)
            driver.close()
    except Exception as e:
        print("FAIL")
        print(e.message)
        driver.close()

def download(url):
    print("Trying to download Selenium Server (Grid)")
    try:
        pageopen(url)
        gotit = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div/p[1]/a')
        gotit.click()

        constant_wait()
        #tu powinno być sprawdzenie czy ten plik się pobrał tak naprawdę jakiś wait czy coś w ten deseń

        print("Download file test case successfully completed")
    except Exception as e:
        print("FAIL")
        print(e.message)
        driver.close()

print("Selenium site check things test start")

if(pageopen(selenium_main)):
    print("opening selenium site test sucesfully completed")
searchphrase()
download(selenium_downloads)

constant_wait()
driver.close()
