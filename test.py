from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

#url access
driver = webdriver.Chrome('/Users/luke/Downloads/chromedriver 2')

#test url
# driver.get('https://www.nytimes.com/2021/04/11/world/middleeast/iran-nuclear-natanz.html?action=click&module=Spotlight&pgtype=Homepage')


#MLA citation function
def mla(link):
    driver.get('{}', link)
    
    first_name1 = ''
    last_name1 = ''
    
    first_name2 = ''
    last_name2 = ''
    
    first_name3 = ''
    last_name3 = ''
    
    # I am thinking of collecting the author names in a dictionary
    
    web_title = ''  #italicize 
    
    web = ''
    
    date = ''

    url = link
    
    if first_name3 != '':
        print(f"{last_name1}, {first_name1}, et al. {web_title}, {web}, {date}, {url}" )                            #finished citation
    elif first_name2 != '':    
        print(f"{last_name1}, {first_name1}, {last_name2}, {first_name2}, {web_title}, {web}, {date}, {url}" )      #finished citation
    else:
        print(f"{last_name1}, {first_name1}, {web_title}, {web}, {date}, {url}" )                                   #finished citation

def apa(link):
    driver.get('{}', link)
    print('Not completed yet')

#input variables
citation_style = ''
hyperlink = ''

#input prompt
while True:
    citation_style = input('Choose Citation Style:\n'
    '1. MLA\n'
    '2. APA\n'
    '3. Exit\n' )

    if citation_style == '3':
        exit()

    hyperlink = input('Please enter website link')

    if citation_style == '1':
        mla(hyperlink)
    elif citation_style == '2':
        apa(hyperlink)
    else:
        print('Invalid choice, please try again')