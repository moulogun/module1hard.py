grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
AverageGrade1 = (sum(grades[0])) / len(grades[0])
AverageGrade2 = (sum(grades[1])) / len(grades[1])
AverageGrade3 = (sum(grades[2])) / len(grades[2])
AverageGrade4 = (sum(grades[3])) / len(grades[3])
AverageGrade5 = (sum(grades[4])) / len(grades[4])
StudentsList = list(students)
StudentsList.sort()
AverageGradesOfStudents = {StudentsList[0]:AverageGrade1 ,
     StudentsList[1]:AverageGrade2 ,
     StudentsList[2]:AverageGrade3 ,
     StudentsList[3]:AverageGrade4 ,
     StudentsList[4]:AverageGrade5}
print("Средние оценки чеников:",AverageGradesOfStudents)
