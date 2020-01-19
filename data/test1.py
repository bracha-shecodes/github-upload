import datetime

time_format = "%Y-%m-%d,%H:%M"
current_time = datetime.datetime.now()
line = ['1', current_time.strftime(time_format)]
print(line)

# s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# line = [str(id), str(datetime.datetime.now())]
# date_obj = datetime.datetime.strptime(bdate, date_format)
#           date_obj = datetime.datetime.strptime(emp_bdate, date_format)

# local = datetime.now()
# print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

# line = f"{str(id)},{datetime.datetime.now()}"
