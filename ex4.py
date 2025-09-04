import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# avab lehe
driver.get("https://the-internet.herokuapp.com/login")

# ootab vajalikke elemente
userbox = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))
passbox = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
loginbutton = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/button')))

time.sleep(1)
userbox.click()
userbox.send_keys("tomsmith")
time.sleep(1)
passbox.click()
passbox.send_keys("SuperSecretPassword!")
time.sleep(1)
loginbutton.click()
time.sleep(2)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "flash success")))
print("success")
driver.quit()