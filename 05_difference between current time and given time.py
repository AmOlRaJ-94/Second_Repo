# 05_Python program to find difference between current time and given time

from datetime import datetime


def diff_time(str1):
    now = datetime.now()
    # print(type(now))
    if str1[-2:] == 'PM' and str1[:2] == '12':
        str2 = now.strftime("%H:%M:%S")
        h2, m2, s2 = int(str2[:2]), int(str2[3:5]), int(str2[7:9])
    elif str1[-2:] == 'PM' or str1[-2:] == 'AM':
        str2 = now.strftime("%I:%M:%S %p")
        # print('str2', str2)
        h2, m2, s2 = int(str2[:2]), int(str2[3:5]), int(str2[7:9])
        # print("h2", h2, 'm2 ', m2)
    elif int(str1[:2]) == 00 :
        str2 = now.strftime("%I:%M:%S")
        h2, m2, s2 = int(str2[:2]), int(str2[3:5]), int(str2[7:9])
    else:
        str2 = now.strftime("%H:%M:%S")
        h2, m2, s2 = int(str2[:2]), int(str2[3:5]), int(str2[7:9])


    if int(str1[:2]) == 00:
        h1 = 12
        # print("h1 00 - ", h1)
    else:
        h1 = int(str1[:2])

    m1 = int(str1[3:5])
    # print("h1 ", h1, 'm1 ', m1)


    t1 = h1 * 60 + m1
    # print("t1 ",t1)
    t2 = h2 * 60 + m2
    # print("t2 ", t2)

    if t1 == t2 :
        print("Both are same times")
        return
    elif t2 > t1 :
        diff = t2 - t1
    else:
        diff = t1 - t2

    h = (int(diff/60))%24
    # print('h ', h)
    m = diff % 60
    # print("m ", m)
    # s = diff % 3600
    # print("s ", s)
    if int(str1[:2]) == 00:
        str2 = now.strftime("%H:%M:%S")
    if str1[-2:] == 'PM' and str1[:2] == '12':
        str2 = now.strftime("%I:%M:%S")

    print(f"Difference between {given_time} and {str2} is {h} Hour and {m} Minute.")


given_time = input("""Give your time format in one of the given format :-
1) HH:MM:SS AM/PM -for 12 Hour format.
2) HH:MM:SS - for 24 Hour format.\n
Now Type here Given Time:- """)
diff_time(given_time)

#-----------------------------------------------------------------------------------

# def diff_time(h1, m1, h2, m2):
#     t1 = h1 * 60 + m1
#     print("t1 ",t1)
#     t2 = h2 * 60 + m2
#     print("t2 ", t2)
#
#     if t1 == t2 :
#         print("Both are same times")
#         return
#     else:
#         diff = t2 - t1
#
#     h = (int(diff/60))%24
#     print('h ', h)
#     m = diff % 60
#     print("m ", m)
#
#     print(h, ':', m)
#
# diff_time(7, 20, 9, 45)
# diff_time(15, 23, 18, 54)
# diff_time(9, 45, 9, 45)
