# Imprting the 'datetime' module
from datetime import datetime

# Creating a date using year, month, day as arguments
birthday = datetime(1991, 9, 14, 6, 00)
print(birthday.year)

# Creating a date using datetime.now()
print(datetime.now())
print(datetime(2018, 1, 1) - datetime(2017, 1, 1))
print(datetime.now()-datetime(2025, 9, 14))

# Parsing a date using strptime
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
print(parsed_date)
print(parsed_date.month)
print(parsed_date.year)

# Rendering a date as a string using strftime
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)

current_date = datetime.now
print(current_date)
current_time = datetime.time
print("The date is ", (date_string), ".")
