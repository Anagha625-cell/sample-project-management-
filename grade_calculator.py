def calculate_grade(marks, max_marks=100):
    """Return percentage and letter grade for a numeric marks value."""
    if not (0 <= marks <= max_marks):
        raise ValueError("Marks must be between 0 and max_marks")
    pct = (marks / max_marks) * 100
    if pct >= 90:
        grade = "A"
    elif pct >= 80:
        grade = "B"
    elif pct >= 70:
        grade = "C"
    elif pct >= 60:
        grade = "D"
    else:
        grade = "F"
    return round(pct, 2), grade

def main():
    try:
        s = input("Enter marks (0-100): ").strip()
        marks = float(s)
        pct, grade = calculate_grade(marks)
        print(f"Percentage: {pct}%  Grade: {grade}")
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()
