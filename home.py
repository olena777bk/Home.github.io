import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.get("https://practice.automationtesting.in/")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
Read_More = driver.find_element_by_id("text-22-sub_row_1-0-2-0-0")
Read_More.click()

Reviews = driver.find_element_by_class_name("reviews_tab")
Reviews.click()

driver.execute_script("window.scrollBy(0, 800);")
Star = driver.find_element_by_class_name("star-5")
Star.click()
time.sleep(3)

Comment = driver.find_element_by_id("comment")
Comment.send_keys("Nice book!")
time.sleep(3)

Name = driver.find_element_by_id("author")
Name.send_keys("OLGA")
time.sleep(3)

Email = driver.find_element_by_id("email")
Email.send_keys("12345ol@bk.ru")
time.sleep(3)

Submit = driver.find_element_by_id("submit")
Submit.click()
time.sleep(3)

driver.quit()

