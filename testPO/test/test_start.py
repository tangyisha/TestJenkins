
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_search():
    driver = webdriver.Chrome()
    # 隐式等待
    driver.implicitly_wait(5)
    driver.get("http://www.baidu.com/")
    print(driver.find_element(By.ID, "su").get_attribute("value"))
    print(driver.find_element(By.ID, "su").get_attribute("class"))

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(By.TAG_NAME, "title")).click()
    






test_search()
