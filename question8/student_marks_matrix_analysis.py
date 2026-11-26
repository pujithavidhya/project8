# Student Marks Matrix Analysis

# Get number of students and subjects
students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

# Create marks matrix
marks = []

for i in range(students):
    row = []
    print("Enter marks for Student", i + 1)

    for j in range(subjects):
        mark = int(input("Subject " + str(j + 1) + ": "))
        row.append(mark)

    marks.append(row)

# Display marks matrix
print("\nStudent Marks Matrix:")
for row in marks:
    print(row)

# Calculate total and average marks
for i in range(students):
    total = sum(marks[i])
    average = total / subjects

    print("\nStudent", i + 1)
    print("Total Marks:", total)
    print("Average Marks:", average)

# Find highest marks in each subject
print("\nHighest Marks in Each Subject:")
for j in range(subjects):
    highest = marks[0][j]

    for i in range(students):
        if marks[i][j] > highest:
            highest = marks[i][j]

    print("Subject", j + 1, ":", highest)