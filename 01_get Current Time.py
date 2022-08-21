# Using time module.
# import time as t

# curr_time = t.strftime("%H:%M:%S", t.localtime())
# print("current time is : ", curr_time)
#-----------------------------------------------------------------
# Using datetime module.
# import datetime as dt
#
# curr_time = dt.datetime.now()
# print(curr_time)

#Using datetime module only for showing time

# from datetime import datetime
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("current Time = ", current_time)

# For 12 hour format

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%I:%M:%S")
print("current Time = ", current_time)
print(type(current_time))