students = {
    "Amit": 85,
    "Rahul": 92,
    "Priya": 78,
    "Sneha": 88,
    "Karan": 95
}

# Print students and marks
for name, marks in students.items():
    print(name, ":", marks)

# Class average
average = sum(students.values()) / len(students)
print("Class Average:", average)

# Student with highest marks
topper = max(students, key=students.get)
print("Highest Marks:", topper, "-", students[topper])
