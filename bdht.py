
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

kw = input("Enter your keywords = ")
service = Service(executable_path='venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://dhthanhit.pythonanywhere.com/")

k = driver.find_element(By.NAME, 'keyword')
k.send_keys(kw)
btn = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')
btn.click()

driver.implicitly_wait(2)
products = driver.find_elements(By.CSS_SELECTOR, '.card-title')

# driver.set_page_load_timeout(360)
# time.sleep(1)
for pro in products:
    print(pro.text if pro else '')
    print('=========')
    # try:
    #     # img = pro.find_element(By.CSS_SELECTOR, 'img')
    #     # title = pro.find_element(By.CSS_SELECTOR, '.card-title')
    #     # price = pro.find_element(By.CSS_SELECTOR, 'p card-text')
    #     # print(img.get_attribute('src'))
    #
    #     # print(price.text)
    #
    # except:
    #     pass
details = driver.find_elements(By.CSS_SELECTOR, 'a.btn.btn-primary')
urls = [d.get_attribute('href') for d in details]
for d in urls:
    driver.get(d)
    d.click()
    comments = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(By.CSS_SELECTOR, '.list-group-item p'))
    for c in comments:
        print(c.text)

driver.quit()
