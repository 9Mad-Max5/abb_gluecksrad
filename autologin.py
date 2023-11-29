import os
import sys
import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from getpass import getpass

# from credentials import *


def random_button(driver, sel_timeout, start=6, end=9):
    buttons = WebDriverWait(driver, sel_timeout).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "responseItem"))
    )
    for button in buttons[random.randint(start, end):10]:
        WebDriverWait(driver, sel_timeout).until(
            EC.element_to_be_clickable((By.XPATH, f'//div[@class="column"]//div[@class="responseItem"][{buttons.index(button)+1}]'))
        ).click()
        break

    return

# username = input("Enter in your username: ")
# password = getpass("Enter in your password: ")
page = "https://smonitor.io/S0037341"

# Pfad zum aktuellen Skript
script_path = os.path.abspath(sys.argv[0])
sel_timeout = 60


# def crawl_amazon(page, username, password, otp=None):
# driver = webdriver.Chrome(os.path.join(script_path,"chromedriver.exe"))
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")  # Optional, but can be useful
# driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
# driver.get(page)

# SignIn_button = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
# SignIn_button.click()

driver = webdriver.Chrome()
driver.get(page)

Continue_button = WebDriverWait(driver, sel_timeout).until(
    EC.presence_of_element_located((By.ID, "buttoncontentmiddle"))
)
Continue_button.click()

random_button(driver=driver, sel_timeout=sel_timeout)
random_button(driver=driver, sel_timeout=sel_timeout, start=0, end=3)
random_button(driver=driver, sel_timeout=sel_timeout)

# # Buttons zwischen 7 und 10 finden
# buttons = driver.find_elements(By.CLASS_NAME, "responseItem")[6:10]
# # Einen zufälligen Button auswählen
# random_button = random.choice(buttons)
# # Auf den ausgewählten Button klicken
# random_button.click()
# sleep(3)
# # Einen zufälligen Index zwischen 6 und 9 auswählen
# random_index = random.randint(6, 9)
# Den Button mit dem zufälligen Index auswählen

# random_button = buttons[random_index]
# # Auf den ausgewählten Button klicken
# random_button.click()

# sleep(3)
# # Einen zufälligen Index zwischen 6 und 9 auswählen
# random_index = random.randint(0,3)
# Den Button mit dem zufälligen Index auswählen


# random_button = buttons[random_index]
# # Auf den ausgewählten Button klicken
# random_button.click()

# sleep(3)
# # Einen zufälligen Index zwischen 6 und 9 auswählen
# random_index = random.randint(6, 9)
# Den Button mit dem zufälligen Index auswählen

# random_button = buttons[random_index]
# # Auf den ausgewählten Button klicken
# random_button.click()

buttons = WebDriverWait(driver, sel_timeout).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "next"))
)
buttons.click()

# Button mit dem Text "Fertig" finden und darauf klicken
fertig_button = WebDriverWait(driver, sel_timeout).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="column"]//div[@class="responseItem"]/span[text()="Fertig"]'))
)
fertig_button.click()

sleep(60)
# # Warte, bis das div-Element mit dem Attribut 'data-automation-id="watch-history"' vorhanden ist
# watch_history_div = WebDriverWait(driver, sel_timeout).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-automation-id="watch-history"]'))
# )

# # Warte bis mindestens eine Checkbox gefunden wird
# checkboxes = WebDriverWait(watch_history_div, sel_timeout).until(
#     EC.presence_of_all_elements_located((By.XPATH, './/input[@type="checkbox"]'))
# )

# # Klicke jede Checkbox an
# for checkbox in checkboxes:
#     checkbox.click()


# Greife auf den HTML-Quellcode der Seite zu
page_source = driver.page_source

# Verwende BeautifulSoup, um die Daten zu scrapen
soup = BeautifulSoup(page_source, "html.parser")

# Hier kannst du nun bs4 verwenden, um die Daten von der Seite zu extrahieren
# Beispiel: Finde alle Links auf der Seite
# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))

# Schließe den WebDriver am Ende
# driver.quit()

# return soup

# # Funktion aufrufen
# soup = crawl_amazon(page=page, username=username, password=password, otp=otp)

# # Checkboxen innerhalb des gewünschten div-Elements finden
# # watch_history_div = soup.find('div', {'data-automation-id': 'watch-history'})
# # checkboxes = watch_history_div.find_all('input', {'type': 'checkbox'})

# # Extrahiere Informationen
# history_items = soup.find('div', {'data-automation-id': 'activity-history-items'})
# items = history_items.find_all('li')
# # print(items)
# with open("output1.html", "w") as file:
#     file.write(str(items))

# print(type(items))

# for item in items:
#     # Extrahiere Datum, Serie, Staffel, Folgennummer und Folgentitel
#     date = item.find('div', {'data-automation-id': 'wh-date-5. November 2023'}).div.text.strip()
#     serie = item.find('a', {'class': '_1NNx6V Nwyhwn'}).text.strip()
#     staffel = serie.split('–')[-1].strip()
#     folgennummer = item.find('p').text.split(':')[0].strip()
#     folgentitel = item.find('p').text.split(':')[1].strip()

#     # Ausgabe der extrahierten Daten
#     print("Datum:", date)
#     print("Serie:", serie)
#     print("Staffel:", staffel)
#     print("Folgennummer:", folgennummer)
#     print("Folgentitel:", folgentitel)
#     # print(soup)
