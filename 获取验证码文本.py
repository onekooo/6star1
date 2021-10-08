# coding = utf-8
import time
from time import sleep
from selenium import webdriver
from PIL import Image
import pytesseract

#打开谷歌浏览器
browser = webdriver.Chrome(r'D:\chromedriver.exe')

#打开首页
browser.get("http://192.168.150.120:8080/baorq-lrb-site")
browser.maximize_window()
time.sleep(3)

#如果需要点击注册按钮
# browser.find_element_by_xpath('//a[contains(text(),"注册")]').click()

#获取验证码图
browser.save_screenshot('picture.png')
ce = browser.find_element_by_id("captchaImg")#具体的id要用F12自行查看
print(ce.location)
left = ce.location['x']
top = ce.location['y']
right = ce.size['width'] + left
height = ce.size['height'] + top
im = Image.open('picture.png')
img = im.crop((left,top,right, height))
img.save('picture2.png')#这里就是截取到的验证码图片
browser.close()

#引入pytesseract识别图片中的验证码
image1 = Image.open('picture2.png')
text = pytesseract.image_to_string(image1)
print(text)