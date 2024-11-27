from datetime import date, datetime
# Check how many days before API Key expires
#start_date = os.getenv("BINANCE_API_KEY_DATE")
#end_date_format = '%Y-%m-%d'
#start_date_format = '%Y-%m-%d'
end_date = "2025-2-20"
start_date = "2024-11-22"
print(f'end Date Type = {type(end_date)}')
print(f'start Date Type = {type(start_date)}')


#datetime_str = '09/19/22'
#========================
from dateutil.parser import parse
 
def convert_to_datetime(input_str, parserinfo=None):
    return parse(input_str, parserinfo=parserinfo)
 
# Example usage
#date_string = '2023-07-25'
result_end_date = convert_to_datetime(end_date)
print(result_end_date)
print(f'Type result_end_date = {type(result_end_date)}')

result_start_date = convert_to_datetime(start_date)
print(result_start_date)
print(f'Type result_end_date = {type(result_start_date)}')


#========================

