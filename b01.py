from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# kw = input("Enter keywords = ")
service = Service(executable_path='venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://vnexpress.net/")

print(driver.title)
# Lay cac the article co css thuoc tinh la item-news
articles = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')
for article in articles:
    try:
        title = article.find_element(By.TAG_NAME, 'h3')
        des = article.find_element(By.CLASS_NAME, 'description')
        img = article.find_element(By.TAG_NAME, 'img')
        print(title.text)
        print(des.text)
        print(img.get_attribute('src'))
        print('========')
    except:
        pass
driver.quit()