#!/usr/bin/env python
# coding: utf-8


import requests
import json
import csv
from bs4 import BeautifulSoup


loginForm = "your login form url"
session = requests.Session()
response = session.get(loginForm)
htmlText = response.text
soup = BeautifulSoup(htmlText, 'html.parser')
#print(soup.prettify())

#print(response.headers)

form = soup.find('form')
inp = form.find('input',type="hidden")
params = {
    'username':'your username',
    'passward':'your passward'
}
# _csrf params
params[inp.get('name')] = inp.get('value') 

#print(str(params))


headers = {
   # 'Set-Cookie': response.headers['Set-Cookie'],
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'your origin url',
    'Referer': 'your login referer url',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

loginUrl = "your login request url"
loginResponse = session.post(loginUrl, data=params, headers=headers)
#print(loginResponse.text)

#print(loginResponse.url)

downloadParams={
    'start_date': 'xxxxxx',
    'end_date': 'xxxxxx',
    'type': 'CSV'
}
soup = BeautifulSoup(loginResponse.text, 'html.parser')
form = soup.find('form')
inp = form.find('input',type="hidden")
# _csrf params
downloadParams[inp.get('name')] = inp.get('value') 
# print(downloadParams)


# modified header for downoload data
headers['Referer'] = "your referer url to download data"


# call to fetch data
downloadUrl = "your download url"
responseData = session.post(downloadUrl, data=downloadParams, headers=headers)
#print(responseData.text)

# sotre csv data to local file
with open('daily_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for line in responseData.iter_lines():
        writer.writerow(line.decode('utf-8').split(','))





