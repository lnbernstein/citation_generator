import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import PySimpleGUI as sg
import urllib.request,time
import re
import sys

print('hi')  # doesnt work yet
print(os.environ.get('driver_path'))

window = sg.Window("Citation Generator", layout) # Creates window


options = Options()  # prevents pop up window
options.headless = True


driver = webdriver.Chrome('/Users/luke/Downloads/chromedriver 2', options=options)
# driver = webdriver.Chrome('/Users/jmoge/Downloads/chromedriver', options=options)

# currently testign with this link 
# 'https://www.nytimes.com/2021/04/12/opinion/biden-economy-culture.html?action=click&module=Opinion&pgtype=Homepage'

def testing(link):  # test for bs4, this is working not that poorly
    driver.get(link)
    time.sleep(4)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    print(soup.find('title').getText())

    authors = [{'class': re.compile('line')}, {'class': re.compile('auth')} , {'class': re.compile('by')}] #items to look for
    souped_authors = []
    for a in authors:
        souped_authors += soup.find_all(attrs=a)
    
    # print(souped_authors)
    souped_authors = list(set(souped_authors)) # removes duplicates

    for s in souped_authors:
        if space_count(s.getText()) == 1: #ideally gets only names but by is still there
            print(s.getText())

    results = soup.body.find_all(attrs=authors) # demonstration of how to use a regualr expression
    print(results)

    date ={'tag':'time', 'name': 'date', 'id':'date', 'class': 'timestamp', 'class':'time'} # this doesnt work
    dates = soup.body.find_all(attrs=date) # this doesnt work
    print(dates)


def mla(link):  # MLA citation function
    
    driver.get(link) # creates 
    
    time.sleep(4)  # lets the javascript load in

    # test = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/article/header/div[5]/div/div[2]/p/span[2]/a')
    # print(test.text)  # test is a selenium object and we get the actual text by calling test.text

    
    name1 = driver.find_element_by_xpath('//*[@id="story"]/header/div[5]/div/div[2]/p/span[2]/a')  # Not global
    name1 = name_flipper(name1.text)
    
    name2 = None  # Not ready
    name2 = name_flipper(name2)
    
    name3 = None # Not ready
    name3 = name_flipper(name3)
    
    web_title = driver.find_element_by_tag_name("h1")  # italicize syntax "\x1B[3m  \x1B[23m" 

    web = driver.find_element_by_css_selector("#app > div > div > div:nth-child(2) > footer > nav > ul.css-1ho5u4o.e5u916q0 > li > a > span:nth-child(2)")  # Not global 
    
    date = driver.find_element_by_tag_name("time")

    url = link


    if web == '':
        web = input('Please enter the name of the website:')
    if date == '':
        date = input('Please enter the date in day month year format:')

    if name3 != '':
        print(f"{name1}, et al. \x1B[3m{web_title.text}\x1B[23m, {web.text}, {date.text}, {url}\n" )  # citation for 3+ author 
    elif name2 != '':    
        print(f"{name1}, {name2}, \x1B[3m{web_title.text}\x1B[23m, {web.text}, {date.text}, {url}\n" )  # citation for 2 authors 
    else:
        print(f"{name1}, \x1B[3m{web_title.text}\x1B[23m, {web.text}, {date.text}, {url}\n" )  # citation for 1 authors
    
    driver.quit()  # this closes the webdriver


def apa(link):  # Not ready yet
    # driver.get('{}', link)
    print('Not completed yet\n')
    pass


def name_flipper(name):  # function to flip author name
    if name == None:
        return('')
    else:
        first = []
        second = []
        for x in range(len(name)):
            if name[x] == ' ':
                first = name[0: (x)]
                second = name[(x+1):]
    return(f"{second}, {first}")


def space_count(s):
    count = 0
    for i in range(0, len(s)):
        if s[i] == ' ':
            count += 1

    return count

citation_style = ''  # input variables
url = ''




def main():
    testing('https://www.nytimes.com/2021/04/12/opinion/biden-economy-culture.html?action=click&module=Opinion&pgtype=Homepage')
    
    citation_style = ''  # input variables
    url = ''

    # while True:  # input prompt
    # citation_style = input('Choose Citation Style:\n'
    # '1. MLA\n'
    # '2. APA\n'
    # '3. Exit\n' )

    # if citation_style == '3':
    #     sys.exit('\nThank you, have a nice day\n')

    # url = input('Please enter website url:\n')

    # if citation_style == '1':
    #     mla(url)
    # elif citation_style == '2':
    #     apa(url)
    # else:
    #     print('Invalid choice, please try again')


if __name__ == "__main__":
    main()
