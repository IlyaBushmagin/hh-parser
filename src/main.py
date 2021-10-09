import requests
import json
import re

url = 'https://api.hh.ru/vacancies/'
keyword = 'Python программист'
per_page = 100

def tags_cleaner(text):
    if text is None:
        return "-"
    cleaner = re.compile(pattern='<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6})')
    text = cleaner.sub("", text)
    return text

def get_meta(page = 0):
    req = requests.get(url = url, params = {'text': keyword, 'per_page': per_page, 'page': page})
    found = req.json()['found']
    pages = req.json()['pages']
    req.close()
    return found, pages

def get_data(page = 0):
    req = requests.get(url = url, params = {'text': keyword, 'per_page': per_page, 'page': page})
    data = req.json()['items']
    req.close()
    return data

def get_description(id):
    req = requests.get(url="https://api.hh.ru/vacancies/" + str(id))
    description = tags_cleaner(req.json()['description'])
    req.close()
    return description

found, pages = get_meta()

for page in range(pages):
    data = get_data(page)
    items = len(data)
    for item in range(items):
        #data[item]['...']
