print("===================================")
print("     STUDENT PERFORMANCE TRACKER")
print("===================================")

students = []

while True:
    try:
        number_of_students = int(input("Enter number of students: "))

        if number_of_students > 0:
            break
        else:
            print("Please enter at least 1 student.")

    except ValueError:
        print("Please enter a valid number.")


for student_number in range(1, number_of_students + 1):

    print(f"\n========== STUDENT {student_number} ==========")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    subjects = []
    marks = []

    print("\nEnter details for 5 subjects:")

    for i in range(1, 6):

        subject = input(f"\nEnter name of Subject {i}: ")

        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))

                if 0 <= mark <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

        subjects.append(subject)
        marks.append(mark)

    while True:
        try:
            attendance = float(
                input("\nEnter attendance percentage (0-100): ")
            )

            if 0 <= attendance <= 100:
                break
            else:
                print("Attendance must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

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

    performance = []

    for i in range(len(subjects)):

        if marks[i] >= 90:
            level = "Excellent"
        elif marks[i] >= 75:
            level = "Good"
        elif marks[i] >= 60:
            level = "Average"
        else:
            level = "Needs Improvement"

        performance.append(level)

    student = {
        "name": name,
        "roll_no": roll_no,
        "subjects": subjects,
        "marks": marks,
        "attendance": attendance,
        "percentage": percentage,
        "grade": grade,
        "gpa": gpa,
        "performance": performance
    }

    students.append(student)


# Final class summary

print("\n\n===================================")
print("         CLASS SUMMARY")
print("===================================")

for student in students:

    print(
        f"{student['name']} | "
        f"Roll: {student['roll_no']} | "
        f"{student['percentage']:.2f}% | "
        f"Grade: {student['grade']} | "
        f"GPA: {student['gpa']}"
    )

print("===================================")
