import time
def exam():
    user = input("""
    Welcome,
    1. Admin Portal
    2. Student Portal
    >>> """)
    if user == '1':
        from admin_Reg import admin
        admin()
    elif user == '2':
        from student_Reg import student
        student()
    else:
        print('Invalid input')
        time.sleep(1)
        exam()
exam()