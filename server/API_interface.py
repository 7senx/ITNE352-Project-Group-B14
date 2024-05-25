import json
import os
from newsapi import NewsApiClient 
api = NewsApiClient(api_key='844863c15fad42cba626fb66d2c24ef2')
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_records")

def get_headlines(criteria,option,client_name):
    if option == '1':
        data = api.get_top_headlines(q=criteria)
    elif option == '2':
        data = api.get_top_headlines(category=criteria)
    elif option == '3':
        data = api.get_top_headlines(country=criteria)
    elif option == '4':
        data = api.get_top_headlines()

    file_path = os.path.join(PATH, f'B14_{client_name}_1.{option}.json')
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)
    
    
def get_sources(criteria,option,client_name):
    if option == '1':
        data = api.get_sources(category=criteria)
    elif option == '2':
        data = api.get_sources(country=criteria)
    elif option == '3':
        data = api.get_sources(language=criteria)
    elif option == '4':
        data = api.get_sources()

    
    file_path = os.path.join(path, f'B14_{client_name}_2.{option}.json')
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)


 