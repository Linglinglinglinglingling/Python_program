def check_enrolment():
    name_query = input('please input the student name  ')
    read_name=open('student_data.txt','r')
    read_enrol=open('enrollment.txt','r')
    id=0
    got_name=False
    for line in read_name:
        line_list=line.split(',')
        if name_query==line_list[1]:
            id=line_list[0]
            got_name=True
            break

    if not got_name:
        print('there is no student '+name_query)
        return None
    else:
        for i in read_enrol:
            list_line=i.split()
            if id==list_line[0]:
                print(list_line[1])
    read_name.close()
    read_enrol.close()

check_enrolment()


