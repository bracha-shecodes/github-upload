import datetime
import calendar




# def is_date_valid(year, month):
#     this_date = '%d/%d' % (month, year)
#     try:
#         time.strptime(this_date, '%m/%Y')
#     except ValueError:
#         return False
#     else:
#         return True

today = str(datetime.datetime.today())
# today_str = str(today)
# start_mm = datetime.datetime(today.year, today.month, 1)
# start_mm1 = datetime.datetime(today.year, today.month)
curr_year = int(today[:4])
curr_month = int(today[5:7])
curr_mmyyyy = (today[:7])
# c = calendar.TextCalendar(calendar.SUNDAY)
# for i in c.itermonthdays(2020, 2):
#     print(i)
print(today, curr_year, curr_month, curr_mmyyyy)


# a= 1
# c = calendar.TextCalendar(calendar.SUNDAY)
# str = c.formatmonth(2020, 2)
# print(str)