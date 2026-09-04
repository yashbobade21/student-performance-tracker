print("===================================")
print("     STUDENT PERFORMANCE TRACKER")
print("===================================")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

subjects = []
marks = []

print("\nEnter details for 5 subjects:")

for i in range(1, 6):
    subject = input(f"\nEnter name of Subject {i}: ")

    while True:
        mark = float(input(f"Enter marks for {subject} (0-100): "))

        if 0 <= mark <= 100:
            break
        else:
            print("Invalid marks! Please enter marks between 0 and 100.")

    subjects.append(subject)
    marks.append(mark)

while True:
    attendance = float(input("\nEnter attendance percentage (0-100): "))

    if 0 <= attendance <= 100:
        break
    else:
        print("Invalid attendance! Please enter a value between 0 and 100.")

total = sum(marks)
percentage = total / len(marks)

if percentage >= 90:
    grade = "A+"
    gpa = 10
elif percentage >= 80:
    grade = "A"
    gpa = 9
elif percentage >= 70:
    grade = "B"
    gpa = 8
elif percentage >= 60:
    grade = "C"
    gpa = 7
elif percentage >= 50:
    grade = "D"
    gpa = 6
else:
    grade = "F"
    gpa = 0

print("\n===================================")
print("        PERFORMANCE REPORT")
print("===================================")

print("Student Name :", name)
print("Roll Number  :", roll_no)

print("\nSubject-wise Performance:")

for i in range(len(subjects)):
    mark = marks[i]

    if mark >= 90:
        performance = "Excellent"
    elif mark >= 75:
        performance = "Good"
    elif mark >= 60:
        performance = "Average"
    else:
        performance = "Needs Improvement"

    print(subjects[i], ":", mark, "->", performance)

print("\nTotal Marks  :", total)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("GPA          :", gpa)
print("Attendance   :", attendance, "%")

if attendance >= 75:
    print("Attendance Status: Eligible")
else:
    print("Attendance Status: Shortage")

print("===================================")
