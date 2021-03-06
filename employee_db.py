import csv
from emp import Employee
import phonenumbers
from phonenumbers import NumberParseException
import datetime
from datetime import datetime


class EmployeeDb(object):
    def __init__(self):
        self.csvfile_emp = 'data/employee.dat'
        self.emp_dict = {}
        self.load_data()
        self.first_row_ind = None


    def add_one(self, emp_id, emp_name, emp_phone, emp_bdate):
        emp = Employee(emp_id, emp_name, emp_phone, emp_bdate)
        self.emp_dict[emp.id] = emp              # add to dict where key = emp_id
        self.first_row_ind = False
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
        with open(in_file, 'r') as f:
            for emp_id in f:
                if emp_id[0:-1] in self.emp_dict:
                    success = self.emp_dict.pop(emp_id.strip())
                    print(f'Employee {emp_id} deleted')
        self.rewrite_data()
        success = True
        return success


    def load_data(self):
        with open(self.csvfile_emp, "r+") as f:
            for line in f:
                id, name, phone, bdate = line.strip().split(',')     #split each line by "," to columns
                self.emp_dict[id] = Employee(id, name, phone, bdate)              # insert into dictionary where id is the key and other values is a list
                self.first_row_ind = False
        # print(f'my self.emp_rec dict {self.emp_dict}')

# adds the line to the end of the file  -- append_new_row
    def append_new_row(self, formatted_emp):
        with open(self.csvfile_emp, 'a', newline='') as f:
            writer = csv.writer(f)
            # if not self.first_row_ind:   # I want to add the new record to a new line
            #     writer.writerow()
            writer.writerow(formatted_emp)


    def rewrite_data(self):
         with open(self.csvfile_emp, 'w', newline='') as f:
            writer = csv.writer(f)
            for entry in self.emp_dict.values():
                writer.writerow(entry.format_emp_row())

    def check_validity(self, phone=None, bdate=None):
        if phone:
            try:
                check_phone = phonenumbers.parse((phone), "IL")  # check if phone number legal
                print("emp phone:", check_phone)
                return True
            except NumberParseException:  # NumberParseException ValueError
                print("The string supplied did not seem to be a phone number")
                return False
        if bdate:
            date_format = '%Y-%m-%d'
            try:
                date_obj = datetime.strptime(bdate, date_format)
                print("birthday is:", date_obj)
                return True
            except ValueError:
                print("Incorrect data format, should be YYYY-MM-DD, Please insert a valid date")
                return False




