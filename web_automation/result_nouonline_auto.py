from selenium import webdriver
import sys
from pathlib import Path
from selenium_stealth import stealth
import time


options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/DELL/AppData/Local/Google/Chrome/User Data')
options.add_argument("start-maximized")
options.add_argument("--no-sandbox")
options.add_argument('--profile-directory=Profile 2')
options.add_argument('----headless=new')

driver = webdriver.Chrome(options=options, executable_path=r"C:/chromedriver_win32/chromedriver.exe")
stealth(driver,
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

driver.get("https://www.nouonline.net")

# # dropdowns = driver.find_elements(by=By.CSS_SELECTOR, value="dropdown-menu")
# # for element in dropdowns:


# #     if element.text == "Students":
# #         element.click()
#
driver.quit()
