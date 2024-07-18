grade_table = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0
}

num_courses = int(input("Enter the number of courses: "))
total_grade_points = 0
total_credits = 0

for i in range(num_courses):
    grade = input(f"Enter the letter grade for course {i+1}: ")
    credit = int(input(f"Enter the number of credits for course {i+1}: "))
    
    # calculating the grade points for given grade
    grade_points = grade_table[grade] * credit
    
# updating totals 
    total_grade_points += grade_points
    total_credits += credit
    
gpa = total_grade_points / total_credits
print(f"Your GPA is {gpa}") 