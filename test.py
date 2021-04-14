
from selenium import webdriver
import urllib.request,time
import re
import sys


driver = webdriver.Chrome('/Users/luke/Downloads/chromedriver 2')

# currently testign with this link 
# 'https://www.nytimes.com/2021/04/12/opinion/biden-economy-culture.html?action=click&module=Opinion&pgtype=Homepage'

# MLA citation function

def mla(link):
    
    driver.get(link)

    time.sleep(8)  # lets the javascript load in

    # test is a selenium object and we get the actual text by calling test.text
    test = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/article/header/div[5]/div/div[2]/p/span[2]/a')
    print(test.text)

    driver.quit()
    name1 = ''
    name1 = name_flipper(name1)
    
    name2 = ''
    name2 = name_flipper(name2)
    
    name3 = ''
    name3 = name_flipper(name3)

    # I am thinking of collecting the author names in a dictionary
    
    web_title = '' # italicize please
    
    web = ''
    
    date = ''

    url = link
    
    if web == '':
        web = input('Please enter the name of the website:')
    if date == '':
        date = input('Please enter the date in day month year format:')

    if name3 != '':
        print(f"{name1}, et al. {web_title}, {web}, {date}, {url}" )  # citation for 1 author 
    elif name2 != '':    
        print(f"{name1}, {name2}, {web_title}, {web}, {date}, {url}" )  # citation for 2 authors 
    else:
        print(f"{name1}, {web_title}, {web}, {date}, {url}" )  # citation for 3+ authors

def apa(link):
    # driver.get('{}', link)
    print('Not completed yet\n')
    pass

def name_flipper(name):  # function to flip author name
    first = []
    second = []
    for x in range(len(name)):
        if name[x] == ' ':
            first = name[0: (x-1)]
            second = name[(x+1): -1]
    return(f"{first} {second}")


citation_style = ''  # input variables
url = ''

while True:  # input prompt
    citation_style = input('Choose Citation Style:\n'
    '1. MLA\n'
    '2. APA\n'
    '3. Exit\n' )

    if citation_style == '3':
        sys.exit('\nThank you, have a nice day\n')

    url = input('Please enter website url:\n')

    print(url)

    if citation_style == '1':
        mla(url)
    elif citation_style == '2':
        apa(url)
    else:
        print('Invalid choice, please try again')