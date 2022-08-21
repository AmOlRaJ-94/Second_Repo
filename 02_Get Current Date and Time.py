# 02_Get Current Date and Time using Python

# from datetime import datetime as dt
#
# current_datetime = dt.now()
# print(current_datetime)

# rearrange date,month,year position
from datetime import datetime

now = datetime.now()
current_datetime = now.strftime("%d-%m-%y %H:%M:%S")
print(current_datetime)
