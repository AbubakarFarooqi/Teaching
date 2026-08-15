def calculate_percentage(marks):
    return sum(marks) / len(marks)
 
def assign_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 60:
        return "B"
    return "C"
 
def print_result(name, marks):
    p = calculate_percentage(marks)
    print(name, p, assign_grade(p))
 
# 50 students is now trivial:
print_result("Ali", [85, 90, 78])
print_result("Sara", [70, 65, 88])
print_result("Ali", [85, 90, 78])
print_result("Sara", [70, 65, 88])
print_result("Ali", [85, 90, 78])
print_result("Sara", [70, 65, 88])
print_result("Ali", [85, 90, 78])
print_result("Sara", [70, 65, 88])
print_result("Ali", [85, 90, 78])
print_result("Sara", [70, 65, 88])
print_result("Ali", [85, 90, 78])
print_result("Sara", [70, 65, 88])
print_result("Ali", [85, 90, 78])
print_result("Sara", [70, 65, 88])
