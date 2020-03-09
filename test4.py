import datetime

hour_format = '%H:%M'
late_time = datetime.datetime.strptime('09:30', hour_format)
line = '900,"2020-01-19,08:32"'
line = line.replace('"', '')
p_id, a_date, a_time = line.strip().split(',')
punch_time = datetime.datetime.strptime(a_time, hour_format)
print(late_time, type(late_time))
# if punch_time.time() > late_time.time():
#     print(p_id, ',', a_date, ',', punch_time, type(punch_time))
# else:
#     print(p_id, ',', a_date, ',', punch_time, type(punch_time), 'ccccc')

print(str(datetime.datetime.now()))
print(str(datetime.datetime.today()))
