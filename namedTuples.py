from collections import namedtuple
if __name__=='__main__':
    n = int(input())
    if n > 0 and n <= 100:
        fields = input()
        student_list = []
        Student = namedtuple('Student', fields)
        for _ in range(n):
            vals = input()
            student_list.append(Student(*vals.split()))
        print('{:.2f}'.format(sum([int(x.MARKS) for x in student_list]) / len(student_list)))