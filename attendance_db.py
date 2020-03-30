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

    def do_current_month_rep(self):
        today = str(datetime.datetime.today())
        curr_mmyyyy = (today[:7])
        print('attendance report of current month  ', curr_mmyyyy, ': ')
        with open(self.csvfile_att, "r") as f:
            cnt = 0
            for line in f:
                line = line.replace('"', '')
                p_id, a_date, a_time = line.strip().split(',')
                if a_date[0:7] == curr_mmyyyy:
                    cnt += 1
                    print(p_id, ' ', a_date)
            print('total: ', cnt)


    def do_late_rep(self):
        csvfile_att = 'data/att.dat'
        hour_format = '%H:%M'
        late_time = datetime.datetime.strptime('09:30', hour_format)
        print('List of employees who were late: ')
        with open(csvfile_att, "r") as f:
            cnt = 0
            for line in f:
                line = line.replace('"', '')
                p_id, a_date, a_time = line.strip().split(',')
                punch_time = datetime.datetime.strptime(a_time, hour_format)
                if punch_time.time() > late_time.time():
                    cnt += 1
                    print(p_id, ',', a_date, ',', punch_time)
            print('total: ', cnt)
