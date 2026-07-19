# grade_report.py

# List of students
students = [
    {"name": "Alice", "maths": 80, "english": 75, "science": 90},
    {"name": "Bob", "maths": 65, "english": 60, "science": 70},
    {"name": "Charlie", "maths": 50, "english": 55, "science": 45},
    {"name": "David", "maths": 90, "english": 95, "science": 85},
    {"name": "Emma", "maths": 35, "english": 40, "science": 30}
]

results = []

total_average = 0
highest = 0
lowest = 100

# Process each student
for student in students:

    average = (student["maths"] + student["english"] + student["science"]) / 3

    # Grade
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Status
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    results.append({
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    })

    total_average += average

    if average > highest:
        highest = average

    if average < lowest:
        lowest = average


# Class statistics
class_average = total_average / len(students)

# Display report
print("\n===== CLASS REPORT =====")

for result in results:
    print("----------------------------")
    print("Name   :", result["name"])
    print("Average:", round(result["average"], 2))
    print("Grade  :", result["grade"])
    print("Status :", result["status"])

print("----------------------------")
print("Class Average:", round(class_average, 2))
print("Highest Average:", round(highest, 2))
print("Lowest Average:", round(lowest, 2))


# Search student
while True:

    search = input("\nEnter student name to search (or type 'exit'): ")

    if search.lower() == "exit":
        print("Program ended.")
        break

    found = False

    for result in results:
        if result["name"].lower() == search.lower():
            print("\nStudent Found")
            print("Name   :", result["name"])
            print("Average:", round(result["average"], 2))
            print("Grade  :", result["grade"])
            print("Status :", result["status"])
            found = True
            break

    if found == False:
        print("Student not found.")