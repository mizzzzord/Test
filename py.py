from selenium import webdriver

driver = webdriver.Chrome()  # Драйвер скачается сам
driver.get("https://google.com")
print(driver.title)
driver.quit()