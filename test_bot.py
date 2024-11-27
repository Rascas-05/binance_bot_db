from binance.client import Client
import logging
from binance.exceptions import BinanceAPIException
#*****Start My code*****
# importing os module for environment variables
import os, time
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
from datetime import date, datetime, timezone
import json, pprint
from dateutil.parser import parse
# loading variables from .env file
load_dotenv() 

# accessing API keys
# Note .env file should be in the root directory as well as trading_bot.py
    
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
#test key
#****************************************************
# TO DO CHECK LIST
#****************************************************
# to do: comment out print Keys
#print(BINANCE_API_KEY)
#print(BINANCE_API_SECRET)
# Test Biance error logging - -> log.json
# SECURITY WARNING: don't run with debug turned on in production!
#****************************************************
client = Client(BINANCE_API_KEY,BINANCE_API_SECRET)

#If your API Key does not have whitelisted IP address(es), i.e. this API Key allows access to any IP address,
#your selected "Enable Spot & Margin Trading" permission will be valid for 90 days from the activation time. 
#The system will automatically uncheck the permission after the expiration date.26 July 2021
BINANCE_API_KEY_WHITE_LISTED = os.getenv("BINANCE_API_KEY_WHITE_LISTED")
  
# Check how many days before API Key expires
#start_date = os.getenv("BINANCE_API_KEY_DATE")
end_date = os.getenv("BINANCE_API_KEY_EXPIRES")
end_date = "2025-2-20"
#print(f'end Date Type = {type(end_date)}')
# end_date is a string so we need to reformat it as a datetime object otherwise we get a dateutil.parser error

print(f'End Date = {end_date}')
print(f'End Date Type = {type(end_date)}')
#Convert a date string to a DateTime Object
def convert_to_datetime(input_str, parserinfo=None):
    return parse(input_str, parserinfo=parserinfo)
 
# Example usage -> date_string = '2023-07-25'
date2 = convert_to_datetime(end_date)
print(date2)
print(f'Type date2 = {type(date2)}')

def numOfDays(date1, date2):
    return (date2-date1).days
     
date1 = datetime.today()
print(f' Today is {date1}')
print(f'Date1 type = {type(date1)}')
print(f'Date2 type = {type(date2)}')
diff = numOfDays(date1, date2)
print(f'Your API key expires in {diff} days')

# Set up the logger to log errors in JSON format
class JsonLogFormatter(logging.Formatter):
    def format(self, record):
        log_message = {
            'time': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
            'exception': record.exc_info,
        }
        return json.dumps(log_message)

logger = logging.getLogger('binance_logger')
logger.setLevel(logging.ERROR)

# Create file handler that logs error messages
file_handler = logging.FileHandler('log.json')
file_handler.setLevel(logging.ERROR)

# Set custom formatter
formatter = JsonLogFormatter()
file_handler.setFormatter(formatter)

# Add file handler to logger
logger.addHandler(file_handler)

# Create file log.json?
if not os.path.exists("log.json"): 
    log = {}
    log['errors'] = "None"
    # write data to log.json file
    with open("log.json", "w") as f:
        json.dump(log, f)
        
#Check we can open log.json file  
try:
  with open("log.json") as f:
    log = json.load(f)
    print("Loading data from log.json file") 
except:
    print("Something went wrong when opening file log.json")
finally:
    f.close()
    
# Create file data.json?
if not os.path.exists("data.json"): 
    data = {}
    
    data['API_KEY_DATE'] = os.getenv("BINANCE_API_KEY_DATE")
    data['API_KEY_EXPIRES'] = os.getenv("BINANCE_API_KEY_EXPIRES")
    data['TESTNET'] = os.getenv("TESTNET")
    data['API_KEY_WHITE_LISTED'] = os.getenv("BINANCE_API_KEY_WHITE_LISTED")
    print("data.json file created")
    # write data to data.json file
    with open("data.json", "w") as f:
        json.dump(data, f)

#Check we can open data.json file  
try:
  with open("data.json") as f:
    data = json.load(f)
    print("Reading data from data.json file")
    print(f"API Created date: {data.get('API_KEY_DATE')}")
    print(f"API Key Expiry date: {data.get('API_KEY_EXPIRES')}")
    print(f"Testnet .env = {data.get('TESTNET')}")
    net = data.get('TESTNET')     
    if net == "True":
        print("Using Binance Testnet")
    else:
        print("Using Binance Mainnet")
    print(f"API Key White Listed? {data.get('API_KEY_WHITE_LISTED')}")
    f.close()  
except:
    print("Something went wrong when opening file data.json")
finally:
    f.close()
    
#*****End My code******
#--------------------------------------------------------
# 5 - Requesting the latest prices from Binance API - Python Trading Bot Full Tutorial - Thomas DB
# https://www.youtube.com/watch?v=xv6_-XRD7hM
#
client = Client(BINANCE_API_KEY,BINANCE_API_SECRET)

# Function to fetch the latest price (Kline data) from Binance
def get_latest_price(client, code):
    try:
        # Get the historical kline (candlestick) data
        latest_price = client.get_historical_klines(code, Client.KLINE_INTERVAL_1MINUTE, "1 minute ago UTC")
        # Return the prettified response
        return prettify_binance_response(latest_price[0])  # Get the first kline in the response
    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {str(e)}", exc_info=True)
        print(f"Error: {str(e)}")
    except Exception as e:
        logger.error(f"General Error: {str(e)}", exc_info=True)
        print(f"Error: {str(e)}")
    return None

# Function to prettify the kline data (convert to a more readable format)
def prettify_binance_response(kline):
    return {
        "open_time": datetime.fromtimestamp(int(str(kline[0])[:10]), tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "open": kline[1],
        "high": kline[2],
        "low": kline[3],
        "close": kline[4],
        "volume": kline[5],
        "close_time": datetime.fromtimestamp(int(str(kline[6])[:10]), tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "quote_asset_volume": kline[7],
        "number_of_trades": kline[8],
        "taker_buy_base_asset_volume": kline[9],
        "taker_buy_quote_asset_volume": kline[10]
    }

# Example call to get and prettify the latest price for BTCUSDT
# response = get_latest_price(client, "BTCUSDT")
# if response:
#     print(response)
# # ```

#======================
# Test code
code = "BTCUSDT"
i = 0
while i < 10:
    #response = prettify_binance_response(get_latest_price(client, code)[0])
    response = get_latest_price(client, code)
    if response:
        print(response)
    time.sleep(10)
    i += 1
#=====================================================================