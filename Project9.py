student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Scores 71 - 80: Grade = "Acceptable" 

# - Scores 70 or lower: Grade = "Fail" 



student_grades = {}
for k in student_scores:

    if 91<=student_scores[k]<=100:
        student_scores[k] = "Outstanding"
        student_grades = student_scores
    elif 81<=student_scores[k]<=90:
        student_scores[k] = "Exceeds expectation"
        student_grades = student_scores
    elif 71<=student_scores[k]<=80:
        student_scores[k] = "Acceptable"
        student_grades = student_scores
    else:
        student_scores[k] = "Fail"
        student_grades = student_scores
print(student_grades)