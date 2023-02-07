import time
from selenium.webdriver.chrome.options import Options
path_to_extension = r'C:\Users\olena\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.create_options()
driver.implicitly_wait(5)
driver.maximize_window()

# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
#
# My_account = driver.find_element_by_id("menu-item-50")
# My_account.click()
# time.sleep(3)
#
# Username = driver.find_element_by_id("username")
# Username.send_keys("olena777bk@gmail.com")
#
# Password1 = driver.find_element_by_id("password")
# Password1.send_keys("789Cnheybyj!@")
#
# Login = driver.find_element_by_css_selector("[name='login']")
# Login.click()
# time.sleep(3)
#
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# time.sleep(3)
#
# HTML5 = driver.find_element_by_css_selector("li.post-181")
# HTML5.click()
#
# HTML5_Forms = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "summary.entry-summary"), "HTML5 Forms"))
# print(HTML5_Forms)
#
# driver.quit()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
#
# My_account = driver.find_element_by_id("menu-item-50")
# My_account.click()
# time.sleep(3)
#
# Username = driver.find_element_by_id("username")
# Username.send_keys("olena777bk@gmail.com")
#
# Password1 = driver.find_element_by_id("password")
# Password1.send_keys("789Cnheybyj!@")
#
# Login = driver.find_element_by_css_selector("[name='login']")
# Login.click()
# time.sleep(3)
#
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# time.sleep(3)
#
# HTML = driver.find_element_by_link_text("HTML")
# HTML.click()
# time.sleep(3)
#
# items_count = driver.find_elements_by_css_selector(".type-product")
# time.sleep(3)
# if len(items_count) == 3:
#     print("Отображается 3 товара")
# else:
#     print("Ошибка. Количество товаров: " + str(len(items_count)))
# time.sleep(3)
#
# driver.quit()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
#
# My_account = driver.find_element_by_id("menu-item-50")
# My_account.click()
# time.sleep(3)
#
# Username = driver.find_element_by_id("username")
# Username.send_keys("olena777bk@gmail.com")
#
# Password1 = driver.find_element_by_id("password")
# Password1.send_keys("789Cnheybyj!@")
#
# Login = driver.find_element_by_css_selector("[name='login']")
# Login.click()
# time.sleep(3)
#
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# time.sleep(3)
#
# from selenium.webdriver.support.select import Select
#
# Status_Selector = driver.find_element_by_class_name("orderby")
# Status_Selector_Default_sorting = Status_Selector.get_attribute("value")
#
# if Status_Selector_Default_sorting == "menu_order":
#     print("По умолчанию стоит значение селектора Default sorting")
# else:
#     print("выбрано другое значение:", Status_Selector_Default_sorting)
#
# high_to_low = driver.find_element_by_class_name("orderby")
# select = Select(high_to_low)
# select.select_by_index(5)
# time.sleep(3)
#
# high_to_low = driver.find_element_by_class_name("orderby")
# Status_high_to_low = high_to_low.get_attribute("value")
#
# if Status_high_to_low == "price-desc":
#     print ("Выбрано значение селектора: high to low")
# else:
#     print("выбрано другое значение:", Status_high_to_low)
# time.sleep(3)
#
# driver.quit()

# ======================================================================================================================

driver.get("https://practice.automationtesting.in/")
time.sleep(3)

My_account = driver.find_element_by_id("menu-item-50")
My_account.click()
time.sleep(3)

Username = driver.find_element_by_id("username")
Username.send_keys("olena777bk@gmail.com")

Password1 = driver.find_element_by_id("password")
Password1.send_keys("789Cnheybyj!@")

Login = driver.find_element_by_css_selector("[name='login']")
Login.click()
time.sleep(3)

Shop = driver.find_element_by_id("menu-item-40")
Shop.click()
time.sleep(3)

Android = driver.find_element_by_css_selector("li.post-169")
Android.click()

Old_price = driver.find_element_by_css_selector(".price > del > span")
Old_price_get_text = Old_price.text
assert Old_price_get_text == "₹600.00"

New_price = driver.find_element_by_css_selector(".price > ins > span")
New_price_get_text = New_price.text
assert New_price_get_text == "₹450.00"

weit = WebDriverWait(driver, 10)

Zoom = weit.until(EC.element_to_be_clickable((By.CLASS_NAME, "images")) )
Zoom.click()

Close = weit.until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) )
Close.click()

# driver.quit()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++











