from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome('/Users/luke/Downloads/chromedriver 2')

driver.get('https://www.nytimes.com/2021/04/11/world/middleeast/iran-nuclear-natanz.html?action=click&module=Spotlight&pgtype=Homepage')

print('hi')
print('jtesting')

def mla(link):
    driver.get('{}', link)
    pass 

def apa(link):
    driver.get('{}', link)
    pass

citation_style = ''
hyperlink = ''
while True:
    print(
        'Choose Citation Style:\n'
        '1. MLA\n'
        '2. APA\n'
        '3. Exit\n'
        )
    input = citation_style

    print(
        'Please enter website link:\n'
        )
    input = hyperlink

    if citation_style == '1':
        mla(hyperlink)
    elif citation_style == '2':
        apa(hyperlink)
    elif citation_style == '3':
        exit()
    else:
        print('Invalid choice, please try again')