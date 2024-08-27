from selenium import webdriver
from time import sleep

driver = webdriver.Edge(r'D:\edgedrive\edgedriver_win64\msedgedriver.exe')
driver.get("https://blog.csdn.net/qq_46028493/article/details/114045412")

print('Before search================')


# from selenium import webdriver
# from msedge.selenium_tools import Edge, EdgeOptions
# options = EdgeOptions()
# options.use_chromium = True
# options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" # 浏览器的位置
# driver = Edge(options=options, executable_path=r"D:\edgedrive\edgedriver_win64\msedgedriver.exe") # 相应的浏览器的驱动位置
# driver.get("http://www.baidu.com")
