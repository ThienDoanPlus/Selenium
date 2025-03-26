from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service(executable_path='venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.conferenceseries.com/past-conference-reports.php")

sections = driver.find_elements()

driver.quit()