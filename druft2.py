import time


def is_date_valid(year, month):
    this_date = '%d/%d' % (month, year)
    try:
        time.strptime(this_date, '%m/%Y')
    except ValueError:
        return False
    else:
        return True


yy = int(input("Enter Year YYYY: "))
mm = int(input("Enter Month MM: "))
success = is_date_valid(yy, mm)
print(success)