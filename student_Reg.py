import time
import sys
import mysql.connector as connection
myconn = connection.connect(host = '127.0.0.1', user = 'root', passwd = 'Oluwadamilola99$$', database = 'exam_portal')
cursor = myconn.cursor()

def student():
    acct = input("""
    Enter 1 to Login
    Enter 2 to create account
    >>> """)
    if acct == '1':
        login()
    elif acct == '2':
        student_reg()
    else:
        print('Invalid input')
        student()

def student_reg():
    querry = 'insert into student_id(first_name, middle_name, last_name, Gender, Course, Email, Passwd) values(%s,%s,%s,%s,%s,%s,%s)'
    print('Creating account >>>')
    time.sleep(1)
    first_name = input('Enter your first name: ')
    middle_name = input('Enter your middle_name: ')
    last_name = input('Enter your middle name: ')
    Gender = input('Enter your Gender: ')
    Course = input('Enter your Course: ')
    Email = input('Enter your Email: ')
    Passwd = input('Enter your Password: ')
    val = (first_name, middle_name, last_name, Gender, Course, Email, Passwd)
    cursor.execute(querry, val)
    myconn.commit()
    print('Registration Succcessful !!')
    time.sleep(2)
    print('LOG IN >>>')
    login()

def login():
    username = input('Email: ')
    passwd = input('Password: ')
    val = (username, passwd)
    querry = 'select * from student_id where Email = %s and Passwd = %s'
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        time.sleep(1)
        print('PROCESSING >>>')
        time.sleep(2)
        print('Login Successful')
        time.sleep(2)
        write_exam()
    else:
        print('Invalid Login details')
        login()

def write_exam():
    std_user = input("""
    1. Write Exam
    2. Logout Portal
    >>> """)
    if std_user == '1':
        std = input("""
        1. Next
        2. Back
        >> """)
        while std != '2':
            from questions import select_question
            time.sleep(2)
            select_question()
        else:
            write_exam()
    elif std_user == '2':
        time.sleep(2)
        print('Log out Successful')
        time.sleep(1)
        student()
    else:
        print('Invalid input')