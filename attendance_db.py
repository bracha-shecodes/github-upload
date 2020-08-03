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
                f_pid = line.strip().split(',')[0]  # insert the first element to variable
                if str(p_id) == f_pid:
                    cnt += 1
                    p_id, a_date, a_time = line.strip().split(',')  # split each line by "," to columns
                    att_date = a_date.strip('"')
                    att_time = a_time.strip('"')
                    print(f"{cnt:3}: {att_date} {att_time}")

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
                    print(f"{int(p_id):7}: {a_date}")
            print('total: ', cnt)

    def do_late_rep(self):
        hour_format = '%H:%M'
        late_time = datetime.datetime.strptime('09:30', hour_format)
        # late_time = datetime.time(9, 30, 00, 00)
        print('List of employees who were late: ')
        with open(self.csvfile_att, "r") as f:
            cnt = 0
            for line in f:
                line = line.replace('"', '')
                p_id, a_date, a_time = line.strip().split(',')
                punch_time = datetime.datetime.strptime(a_time, hour_format)
                if punch_time.time() > late_time.time():
                    cnt += 1
                    print(f"{p_id:6} {a_date} {a_time}")
            print(f"total: {cnt}")
