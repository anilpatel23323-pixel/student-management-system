# Student Result Management System

def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Marks 0 से 100 के बीच होने चाहिए.")

        except ValueError:
            print("Please valid number enter करें.")


def calculate_grade(percentage, passed):
    if not passed:
        return "F"

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "E"


def main():
    print("=" * 45)
    print("   STUDENT RESULT MANAGEMENT SYSTEM")
    print("=" * 45)

    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    subjects = [
        "Mathematics",
        "Physics",
        "Electronics",
        "Programming"
    ]

    marks = {}

    for subject in subjects:
        marks[subject] = get_marks(subject)

    total = sum(marks.values())
    percentage = total / len(subjects)

    passed = all(mark >= 33 for mark in marks.values())

    grade = calculate_grade(percentage, passed)

    print("\n" + "=" * 45)
    print("              STUDENT RESULT")
    print("=" * 45)

    print(f"Name       : {name}")
    print(f"Roll Number: {roll}")

    print("-" * 45)

    for subject, mark in marks.items():
        print(f"{subject:<15}: {mark:.2f}")

    print("-" * 45)

    print(f"Total      : {total:.2f} / 400")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")

    if passed:
        print("Result     : PASS")
    else:
        print("Result     : FAIL")

    print("=" * 45)


if __name__ == "__main__":
    main()