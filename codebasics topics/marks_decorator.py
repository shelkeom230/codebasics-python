"""
write a decorator to check whether marks of student is greater than 35 
if marks < 35, raise exception --> student is failed"""

def check_marks(func):
    def wrapper(marks):
        if marks<35:
            raise ValueError("student is fail")
        return func(marks)
    return wrapper 

@check_marks
def enter_marks(marks):
    if marks>35 and marks<=60:
        return "passed"
    elif marks>60 and marks<80:
        return "Grade B"
    elif marks>=80 and marks<=90:
        return "Grade A"
    elif marks>90 and marks<=100:
        return "Merit"

print(enter_marks(38))     
            