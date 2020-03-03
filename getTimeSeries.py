import requests
from privateKey import privateKeyModule

apod_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&datatype=json&apikey='+privateKeyModule.keyValue
apod_dict = requests.get(apod_url).json()

print(apod_dict)