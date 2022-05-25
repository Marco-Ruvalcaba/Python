from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Configurar las opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\Program Files (x86)\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)


# Se inicializa el navegador
driver.get('https://eltiempo.es')

# Click para aceptar las cookies
WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.'))))\
    .click()

#
WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#term')))\
    .send_keys('Madrid')
