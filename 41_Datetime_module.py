"""In Python, date and time are not built-in types but are handled using built-in datetime module.
This module offers classes to efficiently work with dates, times and intervals, providing many useful methods."""

"""Date Class"""
# Example 1: Creating a Date Object
from datetime import date
d = date(1996, 12, 11)
print(d)

# Example 2: Get Current Date
from datetime import date
t = date.today()
print(f"Current date: {t}")

# Example 3: Accessing Year, Month and Day Attributes
from datetime import date
t = date.today()
print(f"Year: {t.year}, Month: {t.month}, Day: {t.day}")

# Example 4: Create Date from Timestamp
from datetime import datetime
date_time = datetime.fromtimestamp(1887639468)
print(date_time)
print(date_time.date())

# Example 5: Convert Date to String
from datetime import date
t = date.today()
date_str = t.isoformat()
print(date_str)
print(type(date_str))


"""Time class"""
# Example 1: Time object representing time in Python
from datetime import time

# Create time object with hour, minute and second
my_time = time(13, 24, 56)
print("Entered time:", my_time)

# Time object with only minute specified
my_time = time(minute=12)
print("Time with one argument:", my_time)

# Time object with default (00:00:00)
my_time = time()
print("Time without argument:", my_time)


# Example 2: Get hours, minutes, seconds and microseconds
from datetime import time

Time = time(11, 34, 56)
print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)


# Example 3: Convert Time object to String
from datetime import time

# Creating Time object
Time = time(12,24,36,1212)
print("Time Object:", Time)

# Converting Time object to string
Str = Time.isoformat()
print("String Representation:", Str)
print(type(Str))


"""Datetime class"""
# Example 1: DateTime object representing DateTime in Python 
from datetime import datetime

# Initializing constructor
a = datetime(1999, 12, 12)
print(f"DateTime object: {a}")

# Initializing constructor with time parameters as well
a = datetime(1999, 12, 12, 12, 12, 12, 342380)
print(f"DateTime object with time: {a}")


# Example 2: Get year, month, hour, minute and timestamp
from datetime import datetime

a = datetime(1999, 12, 12, 12, 12, 12)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())


# Example 3: Current date and time
from datetime import datetime

# Calling now() function
today = datetime.now()
print("Current date and time is", today)


# Example 4: Convert Python Datetime to String
from datetime import datetime as dt

# Getting current date and time
now = dt.now()
string = dt.isoformat(now)
print(string)
print(type(string))


"""Timezone class"""
from datetime import datetime
from pytz import timezone

format = "%Y-%m-%d %H:%M:%S %Z%z"
now_utc = datetime.now(timezone('UTC')) # Current time in UTC
print(now_utc.strftime(format))

timezones = ['Asia/Kolkata', 'Europe/Kiev', 'America/New_York']
for tzone in timezones:
    now_asia = now_utc.astimezone(timezone(tzone))  # Convert to Asia/Kolkata time zone
    print(now_asia.strftime(format))