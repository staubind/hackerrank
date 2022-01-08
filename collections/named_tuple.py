# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

num_students = int(input())
column_headings = input()
Student = namedtuple('Student', column_headings)
total_score = 0
for num in range(num_students):
    curr_student = Student(*input().split())
    total_score += int(curr_student.MARKS)
print(round(total_score / num_students, 2))
