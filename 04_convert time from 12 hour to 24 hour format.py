# 04_Python program to convert time from 12 hour to 24 hour format


def convert_time(str1):
    if str1[-2:] == 'AM' and str1[:2] == '12':
        return '00' + str1[2:-2]
    elif str1[-2:] == 'AM':
        return str1[:-2]
    elif str1[-2:] == 'PM' and str1[:2] == '12':
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:-2]

# Check all if..elif..else ladder condition
condi1 = "12:00:00 AM"
print(convert_time(condi1))
condi2 = "04:55:25 AM"
print(convert_time(condi2))
condi3 = "12:30:40 PM"
print(convert_time(condi3))
condi4 = "05:18:10 PM"
print(convert_time(condi4))




