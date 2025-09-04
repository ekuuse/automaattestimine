import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# avab google'i otsingu lehe
driver.get("https://google.com/")

# ootab agreeimist nuppu ja vajutab sellele
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="W0wltc"]/div'))).click()

# ootab otsingu kasti ja siis teeb vajalikud tegevused
searchbox = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="APjFqb"]')))
searchbox.click()
searchbox.send_keys("Erki Kuuse")
time.sleep(1)
searchbox.submit()
time.sleep(2)

# salvestab pildi otsingust
driver.save_screenshot('found.png')

driver.quit()