# import this   #pythons Zen
# import sys
import os
from employee_db import EmployeeDb
from attendance_db import AttendanceDb

db_emp = EmployeeDb()
db_att = AttendanceDb()


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
                          3: remove  employee manually
                          4: delete employees using  file
                          5: Mark attendance
                          6: generate attendance report of an employee
                          7: print report for current month for all employees
                          8: print attendance report for all employees who where late (came after 9:30am')
                          0: Quit/Log Out

                          Please enter your choice: """))

        if choice == 1:
            accept_single_emp()
        elif choice == 2:
            add_from_file()
        elif choice == 3:
            delete_single_emp()
        elif choice == 4:
            delete_using_file()
        elif choice == 5:
            mark_attendance()
        elif choice == 6:
            gen_emp_report()
        elif choice == 7:
            current_month_rep()
        elif choice == 8:
            late_rep()
        elif choice == 0:
            exit(0)
        else:
            print("You must only select  0 - 8 ")
            print("Please try again")
            main_menu()

        pass  # print list of choises main


def accept_single_emp():
    emp_id = None
    while not emp_id:
        emp_id = input("Enter New employee id or q to return to main menu: ")  # get employee number from the user

        if emp_id.lower() == 'q':
            break

        if emp_id in db_emp.emp_dict:  # verify that employee doesn't exists in the file
            print('Employee already exists, try again')
            emp_id = None

    emp_name = input('please enter employee name:')

    emp_phone = None
    success = False
    while not emp_phone and not success:
        emp_phone = input('enter phone (digits only):')
        success = db_emp.check_validity(phone=emp_phone)

    emp_bdate = None
    success = False
    while not emp_bdate and not success:
        emp_bdate = input('enter employees birth date (yyyy-mm-dd):')
        success = db_emp.check_validity(bdate=emp_bdate)

    db_emp.add_one(emp_id, emp_name, emp_phone, emp_bdate)


def add_from_file():
    in_file = None
    while not in_file:
        in_file = input("Enter File name or q to return to main menu: ")
        if in_file.lower() == 'q':
            break
        if not in_file:
            in_file = 'data' + os.path.sep + 'new_emp_list.csv'
        db_emp.add_bulk(in_file)


def delete_using_file():
    in_file = None
    while not in_file:
        in_file = input("Enter File name with list of employees to remove  or q to return to main menu: ")
        if in_file.lower() == 'q':
            break
        if not in_file:
            in_file = 'data' + os.path.sep + 'del_emp_list.csv'
        db_emp.remove_bulk(in_file)


def delete_single_emp():
    emp_id = None
    while not emp_id:
        emp_id = input("Enter employee id to delete  or q to return to main menu: ")

        if emp_id.lower() == 'q':
            break

        if emp_id not in db_emp.emp_dict:
            print('Id:', emp_id, ' not found')
            emp_id = None

        if emp_id in db_emp.emp_dict:  # verify that employee doesn't exists in the file
            print('About to delete employee:', db_emp.emp_dict[emp_id])
            success = db_emp.remove_one(emp_id)
            if success:
                print(success, 'deleted !')
            emp_id = None
    exit(12)


def mark_attendance():
    emp_id = None
    while not emp_id:
        emp_id = input("Enter employee to mark attendance  or q to return to main menu: ")
        if emp_id.lower() == 'q':
            break
        if emp_id not in db_emp.emp_dict:
            print('Id:', emp_id, ' not found')
            emp_id = None
        if emp_id in db_emp.emp_dict:
            # db_emp.add_attendance(emp_id)
            db_att.add_attendance(emp_id)
            emp_id = None
    exit(13)


def gen_emp_report():
    emp_id = None
    while not emp_id:
        emp_id = input("Enter employee ID or q to return to main menu: ")
        if emp_id.lower() == 'q':
            break
        if emp_id not in db_emp.emp_dict:
            print('Id:', emp_id, ' not found')
            emp_id = None
        else:
            db_emp.do_emp_report(emp_id)


def current_month_rep():
    in_month = None
    while not in_month:
        in_month = input("Hit enter to create current month attendance report  or q to quit")
        if in_month.lower() == 'q':
            break
        else:
            db_emp.do_current_month_rep()
    exit(14)


def late_rep():
    in_month = None
    while not in_month:
        in_month = input("Hit enter for late attendance report  or q to quit")
        if in_month.lower() == 'q':
            break
        else:
            db_emp.do_late_rep()
    exit(15)



if __name__ == "__main__":
    main()


# print(EmployeeDb.emp_dict.items())