from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome('/Users/luke/Downloads/chromedriver 2')

driver.get('https://www.nytimes.com/2021/04/11/world/middleeast/iran-nuclear-natanz.html?action=click&module=Spotlight&pgtype=Homepage')

print('hi')
print('jtesting')