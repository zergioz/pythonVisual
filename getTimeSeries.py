import requests
import json
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from privateKey import privateKeyModule
from filePath import filepathModule

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
    jsonFile = pd.read_json (filepathModule.filePath+ticker+'.json')
    jsonFile.to_csv (filepathModule.filePath+ticker+'.csv', index = None, header=True)
    print("Finalized CSV convetion")

# not working 
def TableTicker(ticker):
    df = pd.read_json(ticker+'.json')
    df.set_index("Time Series (Daily)", inplace="True")

tickerInput = getInput()
if tickerInput:
    getJson(tickerInput)
    convertToCsv(tickerInput)
    TableTicker(tickerInput)
else:
    print("Sorry, no ticker provided. Exiting now.")
    exit


