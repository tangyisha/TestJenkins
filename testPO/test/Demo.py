import time

from selenium import webdriver

# 启动 Chrome 浏览器
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options = options)
driver.get("https://testerhome.com/")
#隐式等待
#driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT, "登录").click()
#time.sleep(3)
# 显式等待
# element = WebDriverWait(driver, 30, 0.5).until(lambda driver : driver.find_element(By.ID, "user_login"))
# element.send_keys("1491198849@qq.com")

element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "user_login")))
element.send_keys("1491198849@qq.com")

driver.find_element(By.ID, "user_password").send_keys("apple13269835517")
driver.find_element(By.NAME, "commit").click()
driver.quit()
print("passed")




