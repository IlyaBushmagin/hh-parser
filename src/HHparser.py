import requests
import json
import re

url = 'https://api.hh.ru/vacancies/'

def tags_cleaner(text):
    if text is None:
        return text
    cleaner = re.compile(pattern='<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6})')
    text = cleaner.sub("", text)
    return text

def get_meta(keyword):
    found = 0
    pages = 0
    try:
        req = requests.get(url = url, params = {'text': keyword, 'per_page': 100, 'page': 0})
        found = req.json()['found']
        pages = req.json()['pages']
        req.close()
    except:
        print('Request error')
    return found, pages

def get_data(page, keyword):
    data = {}
    try:
        req = requests.get(url = url, params = {'text': keyword, 'per_page': 100, 'page': page})
        data = req.json()['items']
        req.close()
    except:
        print('Request error')
    return data

def get_description(id):
    description = None
    try:
        req = requests.get(url = url + str(id))
        description = tags_cleaner(req.json()['description'])
        req.close()
    except:
        print('Request error')
    return description

def get_fields(vacancy, fields, data):
    for field in fields:
        try:
            if data[field] is None:
                vacancy[field] = data[field]
            else:
                vacancy[field] = str(data[field])
        except:
            vacancy[field] = None

def get_fields_with_subs(vacancy, fields, subfields, data):
    for field in fields:
        vacancy[field] = {}
        for subfield in subfields:
            try:
                if data[field][subfield] is None:
                    vacancy[field][subfield] = data[field][subfield]
                else:
                    vacancy[field][subfield] = str(data[field][subfield])
            except:
                vacancy[field][subfield] = None