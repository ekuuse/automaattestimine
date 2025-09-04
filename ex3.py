import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# avab lehe
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# ootab lisamist nuppu
addbutton = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/button')))

# vajutab nuppu 5 korda
for i in range(5):
    addbutton.click()
    time.sleep(0.1)

# leiab loodud nupud
createdelements = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="elements"]')))
deletebuttons = createdelements.find_elements(By.CLASS_NAME, "added-manually")

# vajutab koik nupud labi
for button in deletebuttons:
    button.click()
    time.sleep(0.1)

driver.quit()