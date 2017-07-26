from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#desired_cap = {'browser': 'chrome', 'build': 'First build', 'browserstack.debug': 'true' }
desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy S5'}

driver = webdriver.Remote(
    command_executor='http://whunmr:x@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print driver.title
driver.quit()