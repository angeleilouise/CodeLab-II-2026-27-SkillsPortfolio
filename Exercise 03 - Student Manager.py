file = open ("Media/studentMarks.txt", "r") # Opens the text file from the Media folder and reads it 

studentData = file.readlines() # Reads all the lines inside the text file and now they are stored in the variable studentData

file.close() # Closes the file after Python finishes reading it 

numberOfStudents = int(studentData[0]) # Begins from the very first item 

print("Number of students:", numberOfStudents) 

students = []

for student in studentData[1:]:
    student = student.strip().split(",")

    studentNumber = int(student[0])
    studentName = student[1]

    courseMark1 = int(student[2])
    courseMark2 = int(student[3])
    courseMark3 = int(student[4])
    examMark = int(student[5])

    courseworkTotal = courseMark1 + courseMark2 + courseMark3
    overallPercentMark = ((courseworkTotal + examMark) / 160) * 100

    if overallPercentMark >= 70:
        grade = "A"
    elif overallPercentMark >= 60:
        grade = "B"
    elif overallPercentMark >= 50:
        grade = "C"
    elif overallPercentMark >= 40: 
        grade = "D"
    else:
        grade = "F"

    students.append([studentNumber, studentName, courseworkTotal, examMark, overallPercentMark, grade])

print(students)

