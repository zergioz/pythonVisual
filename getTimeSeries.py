import requests
import json
from privateKey import privateKeyModule

# get results and save to .json file 
jsonUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&datatype=json&apikey='+privateKeyModule.keyValue
jsonResult = requests.get(jsonUrl).json()

with open('file.json', 'w', encoding='utf-8') as jsonFile:
    json.dump(jsonResult, jsonFile, ensure_ascii=False, indent=4)


