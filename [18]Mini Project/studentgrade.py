
import math
import datetime
import string

# Student information
name = "John"
grades = [85, 90, 88, 92, 95]

# Calculate average grade
average = sum(grades) / len(grades)

# Calculate square root
square_root = math.sqrt(average)

# Get current date
today = datetime.date.today()

# Get alphabet letters
letters = string.ascii_uppercase

# Display information
print("===== STUDENT GRADE REPORT =====")
print("Student Name:", name)
print("Grades:", grades)
print("Average Grade:", average)
print("Square Root:", round(square_root, 2))
print("Date:", today)
print("Alphabet:", letters)
print("================================")
