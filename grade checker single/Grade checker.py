
def get_student_score():
    score = float(input("Enter student score (0 - 100): "))
    return score


def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"



def display_grade(score, grade):
    print(f"\nScore: {score}")
    print(f"Grade: {grade}")



def main():
    score = get_student_score()
    grade = calculate_grade(score)
    display_grade(score, grade)



main()