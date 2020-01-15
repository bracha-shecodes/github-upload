from emp import Employee
import csv

emp_dict = {}

# def main():
#    print("in def main:",__name__)
#    pass


def load_data():
    with open("data/employee.dat", "r+") as f:
        for line in f:
            id, name, phone, bdate = line.strip().split(',')  # split each line by "," to columns
            emp_dict[id] = Employee(id, name, phone, bdate).format_emp_row()  # insert into dictionary where id is the key and other values is a list
            emp_dict[id] = Employee(id, name, phone, bdate)
            # print(emp_dict[id].__dict__)
            print(emp_dict)
            a = 1
    # print(f'my self.emp_rec dict {self.emp_dict}')


def save_data(in_emp_obj):
    with open('data/employee.dat', 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(in_emp_obj)



# if __name__ == "__main__":
#     load_data()
#     emp_obj = Employee(200, 'ravit alef', '0765544332', '1999-01-01')
#     emp_dict[emp_obj.id] = emp_obj
#     save_data(emp_obj.format_emp_row())
#     # for emp_id, emp_obj in emp_dict.items():
#     #     print( emp_obj )

load1 = load_data()
# print(emp_dict.values())
filename = 'yourfile1.txt'
with open(filename, 'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(emp_dict.values())




exit(999)

# fields = ['id', 'name', 'phone', 'bdate']
# filename = 'yourfile.txt'
# print(type(emp_dict))
# print(emp_dict)
# with open(filename, 'wb') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     print(writer.fieldnames)
#     writer.writerows(emp_dict)
