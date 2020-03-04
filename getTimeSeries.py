import requests
import json
from privateKey import privateKeyModule

print("provide TICKER Symbol to fetch")
tickerInput = str(input()) 
jsonUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+tickerInput+'&datatype=json&apikey='+privateKeyModule.keyValue
jsonResult = requests.get(jsonUrl).json()

with open(tickerInput+'.json', 'w', encoding='utf-8') as jsonFile:
    json.dump(jsonResult, jsonFile, ensure_ascii=False, indent=4)


