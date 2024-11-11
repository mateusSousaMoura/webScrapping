import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

options = webdriver.ChromeOptions()
# options.add_argument('full-screen')
options.add_argument('--window-size=400,800')


navegador = webdriver.Chrome(options=options)
navegador.set_window_position(850,0)
navegador.get('https://www.google.com.br/?hl=pt-BR')
sleep(1.5)

# site = BeautifulSoup(navegador.page_source, 'html.parser')
# print(site.prettify())
try:
    # Locate the element by its class name
    element = navegador.find_element(By.TAG_NAME, "textarea")
    element.send_keys('Botafogo escalação')
    element.submit()
    print(element)
except Exception as e:
    print("Element not found:", e)

sleep(1.5)
button = navegador.find_element(By.CSS_SELECTOR, '[style="border-radius:8px"]')
button.click()

# Keeps the browser open until you press Enter
input("Press Enter to close the browser...")
navegador.quit()