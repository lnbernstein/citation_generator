from bs4 import BeautifulSoup
import urllib.request
import re
import sys



#MLA citation function
def mla(link):
    driver.get('{}', link)
    
    name1 = ''
    name1 = name_flipper(name1)
    
    name2 = ''
    name2 = name_flipper(name2)
    
    name3 = ''
    name3 = name_flipper(name3)

    # I am thinking of collecting the author names in a dictionary
    
    web_title = ''  #italicize 
    
    web = ''
    
    date = ''

    url = link
    
    if web = '':
        web = input('Please enter the name of the website:')
    if date = '':
        date = input('Please enter the date in day month year format:')

    if name3 != '':
        print(f"{name1}, et al. {web_title}, {web}, {date}, {url}" )                            #finished citation
    elif name2 != '':    
        print(f"{name1}, {name2}, {web_title}, {web}, {date}, {url}" )                          #finished citation
    else:
        print(f"{name1}, {web_title}, {web}, {date}, {url}" )                                   #finished citation

def apa(link):
    # driver.get('{}', link)
    print('Not completed yet\n')

def name_flipper(name):
    first = []
    second = []
    for x in len(name):
        if name[x] = ' ':
            while x =! len(name)
                second[x] = [x]
            break
        else:
            first[x] = name[x]
    return(second + first)



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
        sys.exit('\nThank you, have a nice day\n')

    hyperlink = input('Please enter website link:\n')

    if citation_style == '1':
        mla(hyperlink)
    elif citation_style == '2':
        apa(hyperlink)
    else:
        print('Invalid choice, please try again')