# Datetime

# datetime is a built-in module in Python that provides classes for
# manipulating dates and times. It allows you to work with dates, times,
# and time intervals in a convenient way.
# it is structured as a module, which means you need to import it before using
# its classes and functions.

# Example usage of datetime module

from datetime import datetime, date, time, timedelta

# Get the current date and time
current_datetime = datetime.now()
print("Current date and time:", current_datetime)

# Get the current date
current_date = date.today()
print("Current date:", current_date)

# different ways to create a date object
# Create a date object for a specific date
specific_date = date(2023, 1, 1)
print("Specific date:", specific_date)

# different structure for date object
# Create a date object using the fromisoformat() method
iso_date = date.fromisoformat('2023-01-01')
print("ISO date:", iso_date)

# Create a date object using the strptime() method
strptime_date = datetime.strptime('2023-01-01', '%Y-%m-%d').date()
print("Strptime date:", strptime_date)

# Create a date object using the today() method
today_date = date.today()
print("Today's date:", today_date)

# Create a date object using the fromtimestamp() method
timestamp_date = date.fromtimestamp(1672531200)
print("Timestamp date:", timestamp_date)

# use d-m-y format to create a date object
# Create a date object using the strptime() method with d-m-y format
date_str = '12-01-2023'
strptime_date_dmy = datetime.strptime(date_str, '%d-%m-%Y').date()

strptime_date_dmy2 = strptime_date_dmy.strftime('%d-%m-%Y')
print("Strptime date (d-m-y):", strptime_date_dmy2)

# Create a date object using the strptime() method with m-d-y format
strptime_date_mdy = strptime_date_dmy.strftime('%m-%d-%Y')
print("Strftime date (m-d-y):", strptime_date_mdy)

# Create a date object using the strptime() method with y-m-d format
strptime_date_ymd = strptime_date_dmy.strftime('%Y-%m-%d')
print("Strftime date (y-m-d):", strptime_date_ymd)

# Create a date object using the strptime() method with y-d-m format
strptime_date_ydm = strptime_date_dmy.strftime('%Y-%d-%m')
print("Strftime date (y-d-m):", strptime_date_ydm)

# using maths
# Perform arithmetic operations with date objects
# Subtract two dates to get a timedelta
date1 = date(2023, 1, 1)
date2 = date(2023, 1, 10)
delta = date2 - date1
print("Difference between dates:", delta)

# Add two dates to get a new date
# You can add a timedelta to a date to get a new date
new_date = date1 + delta
print("New date after adding timedelta:", new_date)

# time object
# Create a time object for a specific time
specific_time = time(12, 30, 45)
print("Specific time:", specific_time)

# 12  hours format
# Create a time object using the strptime() method with 12-hour format
strptime_time_12hr = datetime.strptime('12:30:45 PM',
                                       '%I:%M:%S %p'
                                       ).time()
print("Strptime time (12-hour format):", strptime_time_12hr)
# 24 hours format
# Create a time object using the strptime() method with 24-hour format
strptime_time_24hr = datetime.strptime('12:30:45', '%H:%M:%S').time()
print("Strptime time (24-hour format):", strptime_time_24hr)

# timedelta object
# Create a timedelta object representing a duration of 1 day, 2 hours, and 30
# minutes
duration = timedelta(days=1, hours=2, minutes=30)
print("Duration:", duration)

# You can perform arithmetic operations with datetime objects and timedelta
# objects. For example, you can add or subtract a timedelta from a datetime to
# get a new datetime.

# Add a timedelta to a datetime
new_datetime = current_datetime + duration
print("New date and time after adding duration:", new_datetime)

# Subtract a timedelta from a datetime
new_datetime_subtracted = current_datetime - duration
print("New date and time after subtracting duration:", new_datetime_subtracted)


# Date and Time Formatting

# The datetime module also provides various formatting options for displaying
# dates and times in different formats. You can use the strftime() method to
# format a datetime object as a string.
# Format a datetime object as a string
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
print("Formatted date and time:", formatted_datetime)

# Using math with datetime objects
# You can perform arithmetic operations with datetime objects and timedelta
# objects. For example, you can add or subtract a timedelta from a datetime to
# get a new datetime.

# example of adding a timedelta to a datetime
new_datetime = current_datetime + duration
print("New date and time after adding duration:", new_datetime)
