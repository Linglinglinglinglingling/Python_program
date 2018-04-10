number_of_units = 3
unit_grades = []
total_sum = 0.0

for i in range(number_of_units):
    unit_grades.append(input("Please enter the grade for " + str(i + 1) + " unit: "))
    try:




for grades in unit_grades:
    if grades == "A":
        total_sum += 4.0
    elif grades == "B":
        total_sum += 3.0
    elif grades == "B":
        total_sum += 2.0
    elif grades == "D":
        total_sum += 1.0
    elif grades == "F":
        total_sum += 1.0

print("The GPA of a student is: " + str(total_sum * number_of_units))