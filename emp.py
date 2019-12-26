
class Employee(object):
    def __init__(self, id, name, phone, birth_date):
        self.id = id
        self.name = name
        self.phone = phone
        self.birthdate = birth_date
        print("Employee-->", self.id, self.name, self.phone, self.birthdate)

    def __repr__(self):
        return str(self.id) + ',' + self.name + ',' + str(self.phone) + ',' + self.birthdate

    def format_emp_row(self):
        return [str(self.id), self.name, str(self.phone), self.birthdate]


