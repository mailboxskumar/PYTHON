from selenium import webdriver


# driver = webdriver.Chrome("E:\chromedriver.exe")
# driver.get("https://developer.twitter.com/en/docs/api-reference-index")
# 
# driver.close()

# 
# driver = webdriver.Firefox(executable_path="E:\\geckodriver.exe")
# driver.get("https://developer.twitter.com/en/docs/api-reference-index")
# 
# driver.close()

driver = webdriver.Ie("E:\IEDriverServer.exe")
driver.get("https://developer.twitter.com/en/docs/api-reference-index")

driver.close()