n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

n = len(student_marks[query_name])
s = sum(student_marks[query_name])

avg = s/n
print(format(avg, '.2f'))
