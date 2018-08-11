import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
   final_grades = []
   for x in grades:
       if x < 38:
           final_grades.append(x)
       else:
           mod = x % 5
           next_m = (x - mod) + 5
           if (next_m - x) < 3:
               final_grades.append(next_m)
           else:
               final_grades.append(x)
   return final_grades

if __name__ == '__main__':
    n = int(input())
    grades = []
    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print('\n'.join(map(str, result)))