# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
 #from bs4 import BeautifulSoup
# import urllib.request,time
# import re
# import sys

import PySimpleGUI as sg

layout = [  # Formatting for pop up window
    [sg.Text("Welcome", size=(20, 4))],
    [sg.Button("MLA", size=(20, 4))],
    [sg.Button("APA", size=(20, 4))],
    [sg.Button("Exit", size=(20, 4))]
]

window = sg.Window("Citation Generator", layout, size=(200, 400)) # Creates window

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "MLA":
        print("Enter URL:")

window.close()