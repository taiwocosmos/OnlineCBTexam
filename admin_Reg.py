import time
import mysql.connector as connection
myconn = connection.connect(host = '127.0.0.1', user = 'root', passwd = 'Oluwadamilola99$$', database = 'exam_portal')
cursor = myconn.cursor()
def admin():
    acct = input("""
    Enter 1 to Login
    Enter 2 to create account
    >>> """)
    if acct == '1':
        admin_login()
    elif acct == '2':
        create_new()
    else:
        print('Invalid input')
        admin()

def create_new():
    querry = 'insert into admin_id(first_name, last_name, Faculty, Email, Passwd) values(%s,%s,%s,%s,%s)'
    print('Creating account >>>')
    time.sleep(1)
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    Faculty = input('Enter Faculty: ')
    Email = input('Enter your Email: ')
    Passwd = input('Enter your Password: ')
    val = (first_name, last_name, Faculty, Email, Passwd)
    cursor.execute(querry, val)
    myconn.commit()
    time.sleep(2)
    print('Admin registration Successful !!')
    time.sleep(3)
    print('LOG IN >>>')
    admin_login()

def admin_login():
    username = input('Email: ')
    passwd = input('Password: ')
    val = (username, passwd)
    querry = 'select * from admin_id where Email = %s and Passwd = %s'
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        time.sleep(2)
        print('Login Successful')
        time.sleep(2)
        dec()
    else:
        print('Invalid Login details')
        admin_login()


def dec():
    admin_user = input("""
        1. Set Questions
        2. Logout Portal
        >>> """)
    if admin_user == '1':
        que = input("""
        1. Next
        2. Back
        >>> """)
        while que != '2':
            from questions import exam_questions
            time.sleep(2)
            exam_questions()
            time.sleep(2)
            que = input("""
            1. Next
            2. Back
            >>> """)
        else:
            dec()
    elif admin_user == '2':
        time.sleep(2)
        print('Log out Successful')
        from exam import exam
        time.sleep(2)
        exam()
    else:
        print('Invalid input')
        dec()