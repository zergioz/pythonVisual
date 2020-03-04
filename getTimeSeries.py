import requests
import json
from privateKey import privateKeyModule

print("Provide ticker symbol:")
tickerInput = str(input())


def getJSON(tiker):
    jsonUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+tiker+'&datatype=json&apikey='+privateKeyModule.keyValue
    jsonResult = requests.get(jsonUrl).json()
    with open(tickerInput+'.json', 'w', encoding='utf-8') as jsonFile:
        json.dump(jsonResult, jsonFile, ensure_ascii=False, indent=4) 

if tickerInput: 
   getJSON(tickerInput)
else:
    print("Sorry, no ticker provided. Exiting now.")
    exit

