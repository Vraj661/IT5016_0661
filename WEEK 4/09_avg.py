'''
PROGRAM WHICH IS AVERAGE
NAME VRAJ PRAJAPATI
'''
# write a function to find the average grade of all students

def find_average_grade(student_grades):
    total_grade = sum(grade for _, _, grade in student_grades)
    return total_grade / len(student_grades)

students = (
    ('James',20,85),
    ('Emily',22,90),
    ('Jack',20,95)
)

def main(): 
    
    avg_grade = find_average_grade(students)
    print("Average Grade : ",avg_grade)

main()