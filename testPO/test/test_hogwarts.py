import time
import pytest
from appium.webdriver import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)
        self.driver.get("https://home.testing-studio.com")

    def teardown(self):
        # 强制等待
        time.sleep(3)
        self.driver.quit()

    def test_hogwart(self):
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()


if __name__ == '__main__':
    pytest.main("-q", "test_hogwarts.py")   # 指定测试文件

