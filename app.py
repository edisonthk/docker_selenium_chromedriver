from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('/chromedriver/chromedriver', options=chrome_options)

driver.get('file:///app/test.html');

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end...")
