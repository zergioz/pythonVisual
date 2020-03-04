import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from privateKey import privateKeyModule

filePath = 'C:/Users/Sergio F. Rodriguez/Documents/pythonVisual/'

def getJson(ticker):
    jsonUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&datatype=json&apikey='+privateKeyModule.keyValue
    jsonResult = requests.get(jsonUrl).json()
    with open(ticker+'.json', 'w', encoding='utf-8') as jsonFile:
        json.dump(jsonResult, jsonFile, ensure_ascii=False, indent=4) 
    print("Finalized dowloading ticker JSON file")

def getInput():   
    print("Provide ticker symbol:")
    tickerInput = str(input())
    return tickerInput

def convertToCsv(ticker):
    jsonFile = pd.read_json (filePath+ticker+'.json')
    export_csv = jsonFile.to_csv (filePath+ticker+'.csv', index = None, header=True)
    print("Finalized CSV convetion")

tickerInput = getInput()
if tickerInput:
    getJson(tickerInput)
    convertToCsv(tickerInput)
else:
    print("Sorry, no ticker provided. Exiting now.")
    exit

