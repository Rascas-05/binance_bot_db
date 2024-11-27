from datetime import datetime
newdate = datetime.strptime("22/11/2024", "%d/%m/%Y").strftime("%Y-%m-%d")
print(f'Date conversion = {newdate}')

newdate1 = datetime.strptime("22-11-2024", "%d-%m-%Y").strftime("%Y-%m-%d")
print(f'Date conversion = {newdate1}')

d1 = datetime.now()
print(f'Current date D1 = {d1}')