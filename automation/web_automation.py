from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
import time

# ✅ Setup driver correctly using Service wrapper
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Go to Google
driver.get("https://www.google.com")
time.sleep(2)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("PyAutomate AI")
search_box.submit()

time.sleep(5)
driver.quit()
