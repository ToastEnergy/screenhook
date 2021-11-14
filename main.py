from selenium import webdriver
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://map.infinit7even.xyz')
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end...")