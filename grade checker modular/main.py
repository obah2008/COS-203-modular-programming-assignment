from input_module import get_student_score
from logic_module import calculate_grade
from output_module import display_grade


def main():
    score = get_student_score()
    grade = calculate_grade(score)
    display_grade(score, grade)


main()