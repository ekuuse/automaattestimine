import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# avab lehe
driver.get("https://quotes.toscrape.com")

# laseme lehel laadida 2 sek
time.sleep(2)

# leiab quoteid
quotes = driver.find_elements(By.CLASS_NAME, "quote")

# loopib labi leitud quotide ja prindib data
for element in quotes:
    text = element.find_element(By.CLASS_NAME, "text").text
    author = element.find_element(By.CLASS_NAME, "author").text
    print(text + ' - ' + author)

driver.quit()