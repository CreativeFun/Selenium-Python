# tu dać opis, że jest to tylko na chromie w jakims tam środowisku itd itd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""Ustawienie opcji tak, by nie wyświetlał się komunikat o harmness file"""
Options = webdriver.ChromeOptions()
prefs = {'safebrowsing.enabled': 'false'}
Options.add_experimental_option("prefs", prefs)

selenium_main = "https://www.selenium.dev"
selenium_downloads = "https://www.selenium.dev/downloads/"
loading_time = 5
truesecond = 1
driver = webdriver.Chrome(options=Options)

#ustawienie opcji na to, żeby można było pobrać plik bez wciskania przycisku o harmness file
#z drugiej strony można by to dać w metodę download ale wtedy by należało robić nowego drivera
#a zależało w sumie mi na ciągłości okna bo ładniej wygląda


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

def searchphrase(phrase):

    print("TODO")


def download(url):
    print("Trying to download Selenium Server (Grid)")
    try:
        pageopen(url)
        gotit = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div/p[1]/a')
        gotit.click()
        time.sleep(6)
        #tu powinno być sprawdzenie czy ten plik się pobrał tak naprawdę jakiś wait czy coś w ten deseń
        print("sample test case successfully completed")
    except Exception as e:
        print("FAIL")
        print(e.message)

print("Selenium site check things test start")

pageopen(selenium_main)
searchphrase()
download(selenium_downloads)


driver.close()
