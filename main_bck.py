
    pass   # print list of choises main

def acept_single_emp():
    while True:
        emp_id = input(
            "Enter New employee details id, name, phone , birhtdate (yyyy-mm-dd) , or q to return to main menu: ")       # get employee number from the user
                           # verify that employee doesn't exists in the file
        if emp_id.lower() == 'q':
            main_menu()


        if emp_id in emp_db.emp_dict:
            print('Employee already exists, try again')

        else:
            emp_name = input('please enter employee name:')
            emp_phone = input('enter phone (digits only):')
            emp_bdate = input('enter employees birth date (yyyy-mm-dd):')
            emp = EmployeeDb()
            emp.add_one(emp_id, emp_name, emp_phone, emp_bdate)


def add_from_file():
    exit(11)

def delete_single_emp():
    exit(12)

def delete_from_file():
    exit(13)

if __name__== "__main__":
    main()

