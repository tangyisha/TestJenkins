from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="../driver/chromedriver")
driver.get("https://testerhome.com/")
driver.implicitly_wait(30)
driver.find_element(By.CSS_SELECTOR, "a[href$='sign_in']").click()
wait = WebDriverWait(driver, 30)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#user_login')))

element.send_keys("1491198849@qq.com")
driver.find_element(By.CSS_SELECTOR, "#user_password").send_keys("apple13269835517")
driver.find_element(By.CSS_SELECTOR, "*[name='commit']").click()
driver.quit()
print("passed")


