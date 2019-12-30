
class Employee(object):
    def __init__(self, id, name, phone, birth_date):
        self.id = id
        self.name = name
        self.phone = phone
        self.birthdate = birth_date
        self.list = [str(self.id), self.name, str(self.phone), self.birthdate]
        # print("Employee-->", self.id, self.name, self.phone, self.birthdate)
        print(self.list)

    def __repr__(self):
        return str(self.id) + ',' + self.name + ',' + str(self.phone) + ',' + self.birthdate

    def format_emp_row(self):
        return [str(self.id), self.name, str(self.phone), self.birthdate]


