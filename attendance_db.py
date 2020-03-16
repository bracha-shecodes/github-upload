import datetime
import csv


class AttendanceDb(object):
    def __init__(self):
        self.csvfile_att = 'data/att.dat'

    def add_attendance(self, p_id):
        time_format = '%Y-%m-%d,%H:%M'
        current_time = datetime.datetime.now()
        with open(self.csvfile_att, 'a', newline="") as f:
            writer = csv.writer(f)
            line = [str(p_id), current_time.strftime(time_format)]
            writer.writerow(line)


    def do_emp_report(self, p_id):
        print('attendance report of employee ', p_id, ': ')
        with open(self.csvfile_att, "r") as f:
            cnt = 0
            for line in f:
                if str(p_id) in line:
                    cnt += 1
                    p_id, a_date, a_time = line.strip().split(',')  # split each line by "," to columns
                    st1 = 0
                    print(cnt, ':', a_date.strip('"'), a_time.strip('"'))
