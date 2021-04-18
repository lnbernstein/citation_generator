import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import PySimpleGUI as sg
import urllib.request,time
import re
import sys
layout = [  # Formatting for pop up window
    [

    ]
]
window = sg.Window("Citation Generator", layout) # Creates window

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
window.close()