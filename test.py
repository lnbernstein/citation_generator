import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request,time
import re
import sys

# doesnt work yet
print('hi')
print(os.environ.get('driver_path'))


# prevents pop up window
options = Options()
options.headless = True


# driver = webdriver.Chrome('/Users/luke/Downloads/chromedriver 2', options=options)
driver = webdriver.Chrome('/Users/jmoge/Downloads/chromedriver', options=options)

# currently testign with this link 
# 'https://www.nytimes.com/2021/04/12/opinion/biden-economy-culture.html?action=click&module=Opinion&pgtype=Homepage'

# MLA citation function

def mla(link):
    
    driver.get(link) # creates 
    

    time.sleep(4)  # lets the javascript load in

    test = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/article/header/div[5]/div/div[2]/p/span[2]/a')
    print(test.text)  # test is a selenium object and we get the actual text by calling test.text

    
    name1 = driver.find_element_by_xpath('//*[@id="story"]/header/div[5]/div/div[2]/p/span[2]/a')
    # name1 = name_flipper(name1)
    
    name2 = ' '
    name2 = name_flipper(name2)
    
    name3 = ' '
    name3 = name_flipper(name3)

    
    web_title = driver.find_element_by_tag_name("h1")  # italicize syntax "\x1B[3m  \x1B[23m" 

    web = driver.find_element_by_tag_name("a")
    
    date = driver.find_element_by_tag_name("time")

    url = link


    if web == '':
        web = input('Please enter the name of the website:')
    if date == '':
        date = input('Please enter the date in day month year format:')

    if name3 != ' ':
        print(f"{name1.text}, et al. \x1B[3m{web_title.text}\x1B[23m, {web.text}, {date.text}, {url}" )  # citation for 3+ author 
    elif name2 != ' ':    
        print(f"{name1}, {name2}, \x1B[3m{web_title}\x1B[23m, {web}, {date}, {url}" )  # citation for 2 authors 
    else:
        print(name1.text + web_title.text + web.text + date.text + url)  # citation for 1 authors
    
    driver.quit()  # this closes the webdriver

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
    return(f"{second}, {first}")


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

    if citation_style == '1':
        mla(url)
    elif citation_style == '2':
        apa(url)
    else:
        print('Invalid choice, please try again')