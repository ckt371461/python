from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--disable-notifications")  #不啟用通知

chrome = webdriver.Chrome('C:\python\PySeleniumPost', chrome_options=options)

email = chrome.find_element_by_id("email")
password = chrome.find_element_by_id("pass")
email.send_keys("ckt371461@gmail.com")
password.send_keys("082371461")
login = chrome.find_element_by_xpath('//*[@id="u_0_5_yr"]')
login.click()

chrome.get("https://www.facebook.com/")