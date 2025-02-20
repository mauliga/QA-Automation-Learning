from selenium import webdriver

# Buka browser
driver = webdriver.Chrome()  
driver.get("https://www.google.com")

# Tunggu 5 detik
driver.implicitly_wait(5)

# Tahan browser agar tidak langsung tertutup
input("Tekan ENTER untuk menutup browser...")
driver.quit()


import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Tunggu 10 detik sebelum menutup
time.sleep(10)
driver.quit()
