# teacher, student , youtuber 
class Teacher:
    def teacher_action(self):
        print("i can teach")

class Engineer:
    def engineer_action(self):
        print("i can write code")

class Youtuber:
    def youtuber_action(self):
        print("i can write code and teach")

class Student(Teacher,Youtuber,Engineer):
    pass 

s=Student()
s.teacher_action()
s.engineer_action()
s.youtuber_action()