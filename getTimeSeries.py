import requests
import json
from privateKey import privateKeyModule

def getJSON(ticker):
    jsonUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&datatype=json&apikey='+privateKeyModule.keyValue
    jsonResult = requests.get(jsonUrl).json()
    with open(ticker+'.json', 'w', encoding='utf-8') as jsonFile:
        json.dump(jsonResult, jsonFile, ensure_ascii=False, indent=4) 

def getInput():   
    print("Provide ticker symbol:")
    tickerInput = str(input())
    return tickerInput

tickerInput = getInput()
if tickerInput:
    getJSON(tickerInput)
else:
    print("Sorry, no ticker provided. Exiting now.")
    exit

