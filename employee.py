import phonenumbers
import datetime

class Employee(object):
    def __init__(self, id, name, phone, birth_date):
        self.id = id
        self.name = name
        self.phone = phone
        self.birthdate = birth_date
        print("Employee", self.id, self.name, self.phone, self.birthdate)


    @classmethod  # anotation ?
    def create_new(cls, emp_id, emp_name, emp_phone, emp_bdate):  # validity  checks  like name like sting and phone

        if phonenumbers.parse((emp_phone),"IL"):           #check if phone number legal
            print("emp___________phone:", phonenumbers.parse((emp_phone),"IL"))
            pass
        else:
            print("emp_phone is not legal")
        date_format = '%Y-%m-%d'
        try:
            date_obj = datetime.datetime.strptime(emp_bdate, date_format)
            print("birthday is:", date_obj)
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")

        newEmp = Employee(emp_id, emp_name, emp_phone, emp_bdate)

        return newEmp
