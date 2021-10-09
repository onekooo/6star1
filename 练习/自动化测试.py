from selenium import webdriver
dirver_path = 'D:/chromedriver.exe'
wd = webdriver.Chrome(dirver_path)
wd.implicitly_wait(3)
#使用css_selector 用元素属性选择元素,支持通配符: * ^ $
# wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
wd.get('https://www.baidu.com')
search_box = wd.find_element_by_id('kw')
search_box.send_keys('python\n')
# element = wd.find_element_by_css_selector('a[href*="miitbeian"')
# element = wd.find_element_by_css_selector('a[href^="http"')
# element = wd.find_element_by_css_selector('[class*="result"]')
elements = wd.find_elements_by_css_selector('div[id="content_left"] > div[class*="result"] > h3')
# print(elements)
for e in elements:
    # print(e.get_attribute('innerHTML'))
    print(e.text)

wd.quit()