import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.get("https://practice.automationtesting.in/")
time.sleep(3)
My_account = driver.find_element_by_id("menu-item-50")
My_account.click()
time.sleep(3)

Email = driver.find_element_by_id("reg_email")
Email.send_keys("olena777bk@gmail.com")

Password = driver.find_element_by_id("reg_password")
Password.send_keys("789Cnheybyj!@")

Register = driver.find_element_by_css_selector("[name='register']")
Register.click()

driver.quit()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Username = driver.find_element_by_id("username")
Username.send_keys("olena777bk@gmail.com")

Password1 = driver.find_element_by_id("password")
Password1.send_keys("789Cnheybyj!@")

Login = driver.find_element_by_css_selector("[name='login']")
Login.click()

driver.quit()


