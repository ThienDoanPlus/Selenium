from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
service = Service(executable_path='venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://tiki.vn/ky-luat-ban-than-p190238356.html?spid=190238357")

driver.execute_script("window.scroll(0, 3600)")
comments = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(By.CSS_SELECTOR, '.list-group-item p'))

driver.quit()