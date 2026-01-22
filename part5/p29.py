# from datetime import date
# dt = date.today()
# # dt = date(2024, 6, 15)
# print("Today's date is:", dt)
# print("Year:", dt.year)
# print("Month:", dt.month)
# print("Day:", dt.day) 
# print("Weekday (0=Monday):", dt.weekday())

# from datetime import time
# t = time(14, 30, 45)
# print("Time is:", t)
# print("Hour:", t.hour)
# print("Minute:", t.minute)
# print("Second:", t.second)

# from datetime import datetime
# # dt = datetime(2024, 6, 15, 14, 30, 45)
# dt = datetime.now()
# print("Datetime is:", dt)
# print("Year:", dt.year)
# print("Month:", dt.month)   
# print("Day:", dt.day)
# print("Hour:", dt.hour)
# print("Minute:", dt.minute)
# print("Second:", dt.second)
# print("Weekday (0=Monday):", dt.weekday())

# from datetime import datetime, timedelta
# dt = datetime.now()
# print("Current datetime:", dt)
# delta = timedelta(days=5, hours=3, minutes=30)
# new_dt = dt + delta
# print("New datetime", new_dt) 
# new_dt = dt - delta
# print("New datetime", new_dt) 

# t1 = datetime(2024, 6, 15, 14, 30, 45)
# t2 = datetime(2024, 6, 10, 10, 15, 30)
# delta = t1 - t2
# print("Time difference:", delta)
# print("Days:", delta.days)
# print("Seconds:", delta.seconds)

# from datetime import datetime
# dt = datetime.now()
# formatted_dt = dt.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted datetime:", formatted_dt)
# formatted_dt = dt.strftime("%B %d, %Y")
# print("Formatted datetime:", formatted_dt)
# formatted_dt = dt.strftime("%B %d, %Y %I:%M %p")
# print("Formatted datetime:", formatted_dt)

# from time import sleep
# for i in range(3):
#     print("Iteration", i)
#     sleep(2)  # Pause for 2 seconds
    
#Accept date with dd/mm/yyyy format
#and print days to new year

