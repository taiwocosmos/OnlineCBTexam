import time
import mysql.connector as connection
myconn = connection.connect(host = '127.0.0.1', user = 'root', passwd = 'Oluwadamilola99$$', database = 'exam_portal')
cursor = myconn.cursor()
def exam_questions():
    querry = 'insert into question_id(question, optionA, optionB, optionC, answer) values(%s,%s,%s,%s,%s)'
    question = input('Write Question: ')
    optionA = input('Enter option A: ')
    optionB = input('Enter option B: ')
    optionC = input('Enter option C: ')
    answer = input('Enter Answer: ')
    val = (question, optionA, optionB, optionC, answer)
    cursor.execute(querry, val)
    myconn.commit()

def select_question():
    score = 0
    selected_que = set()
    ques = input("""
    1. Start Exam
    2. Quit
    >> """)
    if ques =='1':
        time.sleep(1)
        print('Processing >>>')
        time.sleep(2)
        que = input("""
        NOTE: Total of 10 questions, each question carries 10marks.

        Enter STOP to Exit

        Enter Question Number >> """)
        while que != 'stop':
            if que not in selected_que:
                val = (que, )
                querry = 'select * from question_id where id = %s'
                cursor.execute(querry, val)
                result = cursor.fetchone()
                if result:
                    time.sleep(2)
                    print(result[1])
                    print(f'(A) {result[2]}')
                    print(f'(B) {result[3]}')
                    print(f'(C) {result[4]}')
                    answer = input('Answer: ').upper().strip()
                    if answer == result[5]:
                        print('CORRECT')
                        score += 10
                    else:
                        print('WRONG')
                selected_que.add(que)
            else:
                print('You\'ve selected this question')
            time.sleep(1)
            que = input("Enter Question Number: ")
    else:
        from student_Reg import write_exam
        write_exam()
    print(score)