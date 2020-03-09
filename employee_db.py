import csv
from emp import Employee
import phonenumbers
from phonenumbers import NumberParseException
import datetime
from datetime import datetime
# test


class EmployeeDb(object):
    def __init__(self):
        self.emp_dict = {}
        self.load_data()


    def add_one(self, emp_id, emp_name, emp_phone, emp_bdate):
        emp = Employee(emp_id, emp_name, emp_phone, emp_bdate)
        self.emp_dict[emp.id] = emp              # add to dict where key = emp_id
        # emp1 = Employee.create_emp_row(emp)
        self.append_new_row(emp.format_emp_row())         # save to file with create_emp_row that create a list with the values to insert


    def remove_one(self, emp_id):
        success = self.emp_dict.pop(emp_id)   # delete the entry from emp_dict
        self.rewrite_data()
        success = True
        return success


    def add_bulk(self, in_file):  # will get the input csv name frorm the user and peform a loop that will send every line to Employee.create_new
        with open(in_file, "r") as f:
            for line in f:
                id, name, phone, bdate = line.strip().split(',')     #split each line by "," to columns

                if id in self.emp_dict:  # verify that employee doesn't exists in the file
                    print('Employee already exists', id, name)
                    # here enter insert to error file, and continue loop
                    continue

                success = self.check_validity(phone=phone)
                if not success:
                    print('invalid phone', id, phone)
                    break
                success = self.check_validity(bdate=bdate)
                if not success:
                    print('invalid bdate', id, bdate)
                    break
                emp_obj = self.emp_dict[id] = Employee(id, name, phone, bdate)
                self.append_new_row(emp_obj.format_emp_row())  # save to file with create_emp_row that create a list with the values to insert

    def remove_bulk(self, in_file):
        # csvfile_emp = 'data/employee.dat'
        with open(in_file, 'r') as f:
            for emp_id in f:
                success = self.emp_dict.pop(emp_id.strip())
        print(self.emp_dict)
        self.rewrite_data()
        success = True
        return success

    def load_data(self):
        csvfile_emp = 'data/employee.dat'
        with open(csvfile_emp,"r+") as f:
            for line in f:
                id, name, phone, bdate = line.strip().split(',')     #split each line by "," to columns
                self.emp_dict[id] = Employee(id, name, phone, bdate)              # insert into dictionary where id is the key and other values is a list
        # print(f'my self.emp_rec dict {self.emp_dict}')

# adds the line to the end of the file  -- append_new_row
    def append_new_row(self, formatted_emp):
        csvfile_emp = 'data/employee.dat'
        with open(csvfile_emp, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(formatted_emp)

    def rewrite_data(self):
        csvfile_emp = 'data/employee.dat'
        with open(csvfile_emp, 'w', newline='') as f:
            writer = csv.writer(f)
            for entry in self.emp_dict.values():
                writer.writerow(entry.format_emp_row())

    def check_validity(self, phone=None, bdate=None):
        if phone:
            try:
                check_phone = phonenumbers.parse((phone), "IL")  # check if phone number legal
                print("emp___________phone:", check_phone)
                return True
            except NumberParseException:  # NumberParseException ValueError
                print("The string supplied did not seem to be a phone number")
                return False
        if bdate:
            date_format = '%Y-%m-%d'
            try:
                date_obj = datetime.datetime.strptime(bdate, date_format)
                print("birthday is:", date_obj)
                return True
            except ValueError:
                print("Incorrect data format, should be YYYY-MM-DD, Please insert a valid date")
                return False



    def do_emp_report(self, p_id):
        csvfile_att = 'data/att.dat'
        print('attendance report of employee ', p_id, ': ')
        with open(csvfile_att, "r") as f:
            cnt = 0
            for line in f:
                if p_id in line:
                    cnt += 1
                    p_id, a_date, a_time = line.strip().split(',')  # split each line by "," to columns
                    st1 = 0
                    print(cnt, ':', a_date.strip('"'), a_time.strip('"'))


    def do_current_month_rep(self):
        today = str(datetime.datetime.today())
        curr_mmyyyy = (today[:7])
        csvfile_att = 'data/att.dat'
        print('attendance report of current month  ', curr_mmyyyy, ': ')
        with open(csvfile_att, "r") as f:
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

    # def add_attendance(self, p_id):
    #     csvfile_att = 'data/att.dat'
    #     time_format = '%Y-%m-%d,%H:%M'
    #     current_time = datetime.datetime.now()
    #     with open(csvfile_att, 'a', newline="") as f:
    #         writer = csv.writer(f)
    #         line = [str(p_id), current_time.strftime(time_format)]
    #         writer.writerow(line)