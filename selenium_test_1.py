from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'D:\Private\facebook_scraper\drivers\chromedriver.exe')
driver.maximize_window()
driver.get("https://facebook.com/")

driver.find_element_by_id("email").send_keys("gihanrcg97@gmail.com")
driver.find_element_by_id("pass").send_keys("gihan@123")
driver.find_element_by_id("loginbutton").click()


driver.find_element_by_name("q").send_keys("Gihan Saranga Siriwardhana")
driver.find_element_by_name("q").send_keys(Keys.ENTER)

driver.find_element_by_link_text("Gihan Saranga Siriwardhana").click()

driver.execute_script("window.scrollTo(0,1538.4000244140625)")


time.sleep(10)

