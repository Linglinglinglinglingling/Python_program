def calculate_GPA(grade_list):
    total_sum = 0.0
    gpa = 0.0

    for grade in grade_list:
        try:
            if grade.upper() == "A":
                total_sum += 4.0
            elif grade.upper() == "B":
                total_sum += 3.0
            elif grade.upper() == "C":
                total_sum += 2.0
            elif grade.upper() == "D":
                total_sum += 1.0
            elif grade.upper() == "F":
                total_sum += 0.0
        except AttributeError:
            return -2
        else:
            return -1

    gpa = float(total_sum / len(grade_list))
    return gpa