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

def get_items(page, keyword):
    data = {}
    try:
        req = requests.get(url = url, params = {'text': keyword, 'per_page': 100, 'page': page})
        data = req.json()['items']
        req.close()
    except:
        print('Request error')
    return data

def get_description(id):
    data = {'description': None}
    try:
        req = requests.get(url = url + str(id))
        data['description'] = tags_cleaner(req.json()['description'])
        req.close()
    except:
        print('Request error')
    return data

def get_fields(fields, item):
    data = {}
    for field in fields:
        try:
            if item[field] is None:
                data[field] = item[field]
            else:
                data[field] = str(item[field])
        except:
            data[field] = None
    return data

def get_subfields(fields, subfields, item):
    data = {}
    for field in fields:
        data[field] = {}
        for subfield in subfields:
            try:
                if item[field][subfield] is None:
                    data[field][subfield] = item[field][subfield]
                else:
                    data[field][subfield] = str(item[field][subfield])
            except:
                data[field][subfield] = None
    return data