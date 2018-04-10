number_of_units = 3
unit_grades = []
total_sum = 0.0
valid_list=['A','B','C','D','E','F']

for i in range(number_of_units):
    try:
        user_input= input("Please enter the grade for " + (i+1) + " unit: ")
    except:
        print('error')
    else:
    # assert (user_input in valid_list),'invalid input'
    # unit_grades.append(user_input)

        else:
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

            print("The GPA of a student is: " + str((total_sum / number_of_units)))