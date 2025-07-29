#How to calculate maximum value in a list. 

#Way 1
student_marks = [87, 23, 45, 92, 76, 15, 68, 39, 51, 94]
max_score = 0
for marks in student_marks: 
    if max_score < marks:
        max_score = marks
print (max_score)

#Way 2
print(max(student_marks))
