from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

#url access
driver = webdriver.Chrome('/Users/luke/Downloads/chromedriver 2')

#test url
driver.get('https://www.nytimes.com/2021/04/11/world/middleeast/iran-nuclear-natanz.html?action=click&module=Spotlight&pgtype=Homepage')


#MLA citation function
def mla(link):
    driver.get('{}', link)
    author1 = ''
    author2 = ''
    author3 = ''
    web_title = ''  #italicize 

    print('', )     #finished citation
    pass 

def apa(link):
    driver.get('{}', link)
    print('Not completed yet')

#input variables
citation_style = ''
hyperlink = ''

#input prompt
while True:
    print(
        'Choose Citation Style:\n'
        '1. MLA\n'
        '2. APA\n'
        '3. Exit\n'
        )
    input = citation_style

    print('Please enter website link:\n')
    input = hyperlink

    if citation_style == '1':
        mla(hyperlink)
    elif citation_style == '2':
        apa(hyperlink)
    elif citation_style == '3':
        exit()
    else:
        print('Invalid choice, please try again')