from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get('https://google.com')
driver.find_element(By.XPATH, '//input[@name="q"]').send_keys('Almaty Weather' + Keys.RETURN)
sleep(2)
driver.save_screenshot('google_search_almaty_weather.png')
driver.quit()


