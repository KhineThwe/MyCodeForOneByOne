#get current date and time 

# import datetime
# datetime_object = datetime.datetime.now()
# print(datetime_object)

# #to get current date 
# current_date =datetime.date.today()
# print("current_date ",current_date)

# #What is inside datetime module?
# print(dir(datetime))

from datetime import date

today = date.today()

print("Current date =", today)
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
