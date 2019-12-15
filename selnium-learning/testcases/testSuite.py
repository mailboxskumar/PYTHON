from selenium import webdriver

driver = webdriver.chrome("E:\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("https://developer.twitter.com/")
