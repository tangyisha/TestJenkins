from appium import webdriver

desired_caps={}
desired_caps["platformName"] = "Android"
desired_caps["deviceName"] = "127.0.0.1:62001"
desired_caps["appPackage"] = "com.xueqiu.android"
desired_caps["appActivity"] = ".view.WelcomeActivityAlias"

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)
driver.find_element_by_id("tv_agree").click()
# driver.swipe(500, 700, 200, 400, 1000)
# driver.swipe(500, 700, 200, 400, 1000)
# driver.swipe(500, 700, 200, 400, 1000)
# driver.swipe(500, 700, 200, 400, 1000)

print(driver.get_performance_data_types())
print(driver.get_performance_data('com.xueqiu.android', 'cpuinfo', 10))
print(driver.get_performance_data('com.xueqiu.android', 'batteryinfo', 10))
print(driver.get_performance_data('com.xueqiu.android', 'memoryinfo', 10))
print(driver.get_performance_data('com.xueqiu.android', 'networkinfo', 10))


driver.contexts.last
driver.switch_to.default_content()
context = driver.current_context
context = driver.context




