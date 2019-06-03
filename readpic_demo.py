from selenium import webdriver
from PIL import Image
from PIL import ImageEnhance
import pytesseract
import time
import os


driver = webdriver.Chrome()
url = 'https://www.crov.com/'
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_class_name("icon-personal").click()
driver.find_element_by_link_text("Register").click()
driver.save_screenshot('./image/i.png')
#定位验证码
imgelement =driver.find_element_by_id('faptcha_image_img')
location = imgelement.location           #获取验证码x,y坐标
# print(location)
size = imgelement.size           #获取验证码长宽
# print(size)
coderange = (int(location['x']),int(location['y']),int(location['x'] + size['width']),int(location['y'] + size['height']))     #写成我们需要截取的位置坐标
# print(coderange)
openi= Image.open('./image/i.png')     #打开截图
pic1 = openi.crop(coderange)        #使用image的crop函数，从截图中再次截取需要的区域
pic1.save('./image/i2.png')
pic2 = Image.open('./image/i2.png')
pic3 = pic2.convert('L')         #图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
threshold = 160
table = []
for i in range(256):
    if i< threshold:
        table.append(0)
    else:
        table.append(1)
pic3 = pic3.point(table,'1')
pic3.save('./image/i3.jpg')
# sharpness =ImageEnhance.Contrast(pic3)        #对比度增强
# pic4 = sharpness.enhance(3.0)        #3.0为图像的饱和度
# pic4.save('./image/i3.jpg')
openi3 = Image.open('./image/i3.jpg')
text = pytesseract.image_to_string(openi3).strip()
print (text)


def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path,i)
        if os.path.isfilhote(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)