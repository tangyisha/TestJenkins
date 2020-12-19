from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

desired_caps={}
desired_caps["platformName"] = "Android"
desired_caps["deviceName"] = "127.0.0.1:62001"
desired_caps["appPackage"] = "com.xueqiu.android"
desired_caps["appActivity"] = ".view.WelcomeActivityAlias"

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)

# 弹出允许授权框，点击同意
driver.find_element_by_id("tv_agree").click()
# 点击交易
driver.find_element_by_xpath("//*[@text='交易']").click()


# 等待WebView页面加载
WebDriverWait(driver, 20).until(lambda x:x.find_element_by_class_name('android.webkit.WebView'))
# 获取所有WebView并打印显示
contexts = driver.contexts
print(contexts)

# 转换到此apk关联的WebView；根据Chrome浏览器定位到邮箱输入框，输入并提交

# driver.switch_to.context('WEBVIEW_com.wondershare.drfone')

# 转换回到Android原生的WebView；点击左上角返回键
# driver.switch_to.context('NATIVE_APP')




