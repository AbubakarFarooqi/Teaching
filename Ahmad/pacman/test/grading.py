def assign_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    return "C"

if __name__ == "__main__":
    perc = int(input("ye h grading wala module"))
    grade = assign_grade(perc)
    print(grade)