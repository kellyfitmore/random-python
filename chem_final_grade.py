#Stephen Duncanson's program to calculate final chem grades

total = 0

#exams are worth 30%
#collect the three exam scores
exam_grades = []
while len(exam_grades) != 3:
    exam_grade = float(input("Enter an exam score: "))
    exam_grades.append(exam_grade)

#Sort the exams from lowest to highest
exam_grades.sort()
#Remove the lowest score, stored in the [0] index
exam_grades.remove(exam_grades[0])

print("Your two highest exam grades are:")
print(exam_grades)

#lab grade is worth 30%
lab_grade = float(input("Enter your overall laboratory grade: "))

quizzes = []
while len(quizzes) != 8:
    quiz_grade = float(input("Enter a quiz grade: "))
    quizzes.append(quiz_grade)

quizzes.sort()
quizzes.remove(quizzes[0])
print("Your best 7 quizzes are:")
print(quizzes)
#quizzes are worth 15%

#final exam is 25%

#calculate the final grade pre final

exam_average = .30*(sum(exam_grades)/len(exam_grades))
quiz_average = 1.5*(sum(quizzes)/len(quizzes))
lab_grade = .30*lab_grade

pre_final = (exam_average + quiz_average + lab_grade)
#print(pre_final)

for x in range(50, 100, 5):
    final_grade = (x*.25)+pre_final
    print("If you get an",x," on the exam, you get a", final_grade)
