import csv
from emp import Employee
import phonenumbers
from phonenumbers import NumberParseException
import datetime
# test


class EmployeeDb(object):
    def __init__(self):
        self.emp_dict = {}
        self.load_data()


    def add_one(self, emp_id, emp_name, emp_phone, emp_bdate):
        emp = Employee.create_new(emp_id, emp_name, emp_phone, emp_bdate)
        self.emp_dict[emp.id] = emp              # add to dict where key = emp_id
        # emp1 = Employee.create_emp_row(emp)
        self.save_data(emp.format_emp_row())         # save to file with create_emp_row that create a list with the values to insert


    def remove_one(self, emp_id):
        success = self.emp_dict.pop(emp_id)
        print(1)
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
                self.emp_dict[id] = Employee(id, name, phone, bdate)
                emp_obj = Employee(id, name, phone, bdate)
                self.save_data(emp_obj.format_emp_row())  # save to file with create_emp_row that create a list with the values to insert


    def del_bulk(self):
        pass

    def load_data(self):
        with open("data/employee.dat","r+") as f:
            for line in f:
                id, name, phone, bdate = line.strip().split(',')     #split each line by "," to columns
                self.emp_dict[id] = Employee(id, name, phone, bdate)              # insert into dictionary where id is the key and other values is a list
        # print(f'my self.emp_rec dict {self.emp_dict}')

# adds the line to the end of the file
    def save_data(self, formated_emp):
        with open('data/employee.dat', 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(formated_emp)

    def rewrite_data(self, formated_emp):
        with open('data/employee.dat', 'w') as f:
            writer = csv.writer(f)
            write = csv.DictWriter(f, formated_emp)




    def check_validity(self, phone = None, bdate = None):
        if phone:
            try:
                check_phone = phonenumbers.parse((phone), "IL")  # check if phone number legal
                # print("phone:", check_phone)
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



