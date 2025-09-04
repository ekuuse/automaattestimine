import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# avab lehe
driver.get("https://the-internet.herokuapp.com/")

# navigeerib checkbox lehele
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/ul/li[6]/a'))).click()
time.sleep(2)

# leiab checkboxid
checkboxes = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkboxes"]'))).find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

#vajutab nendele
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(0.1)

time.sleep(2)
driver.quit()