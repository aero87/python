#!/usr/bin/python3
from GoogleNews import GoogleNews
googlenews = GoogleNews()
googlenews = GoogleNews(period='7d')
country = input('Type in the country you want to get news from: ')
googlenews.search(country)
result=googlenews.result()
for x in result:
    print("-"*50)
    print("Title--",x['title'])
    print("Date/time--",x['date'])
    print("Description--",x['desc'])
    print("Link--",x['link'])