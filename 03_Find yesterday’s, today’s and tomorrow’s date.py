# 03_Python | Find yesterday’s, today’s and tomorrow’s date

#Using datetime method and timedelta class from datetime module

from datetime import datetime, timedelta

now = datetime.now()
today_date = now.strftime("%d-%m-%y")
print("Today's Date = ", today_date)

yesterday_date = now - timedelta(1)
print("Yesterday's Date = ", yesterday_date.strftime("%d-%m-%y"))

tomorrow_date = now + timedelta(1)
print("Tomorrow's Date = ", tomorrow_date.strftime("%d-%m-%y"))
