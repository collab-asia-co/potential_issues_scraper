//Many of these should be removed, they are just copied and pasted
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import csv
from googleapiclient import errors
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
import os
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import time
import json
import csv
import tkinter as tk
from tkinter import simpledialog
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtubepartner',
    'https://www.googleapis.com/auth/yt-analytics-monetary.readonly',
    'https://www.googleapis.com/auth/yt-analytics.readonly', 
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive', 
    'https://www.googleapis.com/auth/script.external_request',
    'https://www.googleapis.com/auth/script.scriptapp',
    'https://www.googleapis.com/auth/script.send_mail',
    ]

//Below is also just for future use

creds = ServiceAccountCredentials.from_json_keyfile_name('.credentials.json', scope)

client = gspread.authorize(creds)

//Code starts here. 

parent_directory = os.getcwd()
chrome_driver_directory = parent_directory + '/chromedriver'
download_directory = os.getcwd() + '/Downloads/'

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : download_directory}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path= chrome_driver_directory, options=chromeOptions)
driver.get('https://accounts.google.com/servicelogin')

ROOT = tk.Tk()
ROOT.withdraw()

user_input = tk.messagebox.askquestion("Completed Login", "Now log in, and indicate once you are done. \n Have you completed login?", icon='warning', type='yesnocancel')
ROOT.destroy() 

output_sheet = client.open_by_key('1rKpEu60UiuIpHsPqx3Dq36b_uPzCVnzfOJ5BJ6CqgEA').worksheet('Additions')

for cms_id in ['spjVqY2uSt1Ka9RqntE15g', 'gRKGrdXpuJU_NvauhuOD9A','j-kzZLfTxkpSeiLsPVbDMg','TbRYh8_8m5bKt22ytII2Kw','bGKc_BVk-gmsgBM8xcFzag']: 
    asset_id_array = []
    expiration_date_array = []
    issue_type_array = [] 
    next_button = 'Placeholder'
    issues_overview_url = "https://studio.youtube.com/owner/" + cms_id + "/issues?o=" + cms_id + "&filter=%5B%7B%22isPinned%22%3Atrue%2C%22name%22%3A%22STATUS%22%2C%22value%22%3A%5B%22ACTION_REQUIRED%22%5D%7D%5D&sort=%7B%22columnType%22%3A%22viewsLifetime%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D" 
    driver.get(issues_overview_url)
    while next_button != None: 
        time.sleep(5)
        driver.implicitly_wait(10)
        firstLevelMenu = driver.find_elements_by_id("asset-link")
        for asset_link in firstLevelMenu: 
            asset_id_array.append(asset_link.get_attribute('href')[-16:])

        expiration_dates = driver.find_elements_by_id('issue-expiration')
        for expiration_date in expiration_dates: 
            expiration_date_array.append(expiration_date.text[0:2])

        issueTypeMenu = driver.find_elements_by_id("issue-type-container")
        for issue_type in issueTypeMenu: 
            issue_type_array.append(issue_type.text)

        
        try: 
            next_button = driver.find_element_by_id("navigate-after")
            if next_button.get_attribute('aria-disabled') != "true": 
                next_button.click()
            else: 
                next_button = None
        except: 
            next_button = None
        print(f"Current lengths: Asset ID array - {len(asset_id_array)}, Issue Type Array - {len(issue_type_array)} ")
    print(f"Asset id array is: {asset_id_array}, length is {len(asset_id_array)})")
    print(f"Expiration array is: {expiration_date_array}, length is {len(expiration_date_array)})")
    print(f"Issue Type array is: {issue_type_array}, length is {len(issue_type_array)})")



    for i in range(len(issue_type_array)): 
        row = [cms_id,asset_id_array[i],expiration_date_array[i],issue_type_array[i]]
        output_sheet.insert_row(row,i + 1)
        time.sleep(2)
        print(f"Index number {i}, data is {row}")
    #Hover over 

