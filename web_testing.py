from selenium import webdriver

driver = webdriver.Firefox()
driver.get(url="http://localhost:8000/")
assert "The install worked successfully! Congratulations!" in driver.title
