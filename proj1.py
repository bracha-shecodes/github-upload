# import this   #pythons Zen
# import sys
import os
from employee_db import EmployeeDb



emp_db = EmployeeDb()


def main():
    main_menu()

    print("in def main:", __name__)
    pass


def main_menu():
    while True:

        print("************MAIN MENU**************")
        # time.sleep(1)
        print()

        choice = int(input("""
                          1: Add employee manually
                          2: Add employees from file
                          3: Delete employee manually
                          4: delete employees from file
                          5: mark attendance
                          6: generate attendance report of an employee
                          7: print report for current month for all employees
                          8: print attendance report for all employees who where late (came after 9:30am')
                          0: Quit/Log Out

                          Please enter your choice: """))

        if choice == 1:
            acept_single_emp()
        elif choice == 2:
            add_from_file()
        elif choice == 3:
            delete_single_emp()
        elif choice == 4:
            delete_from_file()
        elif choice == 0:
            exit(0)
        else:
            print("You must only select  0 - 8 ")
            print("Please try again")
            main_menu()

        pass  # print list of choises main


def acept_single_emp():
    emp_id = None
    while not emp_id:
        emp_id = input("Enter New employee id or q to return to main menu: ")  # get employee number from the user

        if emp_id.lower() == 'q':
             break

        if emp_id in emp_db.emp_dict:  # verify that employee doesn't exists in the file
            print('Employee already exists, try again')
            emp_id = None

    emp_name = input('please enter employee name:')

    emp_phone = None
    success = False
    while not emp_phone and not success:
        emp_phone = input('enter phone (digits only):')
        success = emp_db.check_validity(phone = emp_phone)

    emp_bdate = None
    success = False
    while not emp_bdate and not success:
        emp_bdate = input('enter employees birth date (yyyy-mm-dd):')
        success = emp_db.check_validity(bdate = emp_bdate)

    emp_db.add_one(emp_id, emp_name, emp_phone, emp_bdate)



def add_from_file():
    in_file = None
    while not in_file:
        in_file = input("Enter File name or q to return to main menu: ")
        if in_file.lower() == 'q':
            break
        if not in_file:
            in_file = 'data' + os.path.sep + 'new_emp_list.csv'



        emp_db.add_bulk(in_file)


def delete_single_emp():
    emp_id = None
    while not emp_id:
        emp_id = input("Enter employee id to delete  or q to return to main menu: ")

        if emp_id.lower() == 'q':
            break

        if emp_id not in emp_db.emp_dict:
            print('Id:', emp_id,' not found')
            emp_id = None

        if emp_id in emp_db.emp_dict:  # verify that employee doesn't exists in the file
            print('About to delete employee:', emp_db.emp_dict[emp_id])
            success = emp_db.remove_one(emp_id)
            if success:
                print(success, 'deleted !')
            emp_id = None
    exit(12)


def delete_from_file():
    exit(13)


if __name__ == "__main__":
    main()

# def find_id_by_name(name,db):
#     list_values = [key for key, val in db.emp_dict.items() if val == name]
#     return db.emp_dict

print(EmployeeDb.emp_dict.items())