def get_student_score() -> float:

    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            print("Invalid input! Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric score.")

def calculate_grade(score: float) -> str:
    
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F' 
    
student_score = get_student_score()
student_grade = calculate_grade(student_score)

print(f"Your Grade is: {student_grade}")
