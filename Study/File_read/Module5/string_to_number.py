read_file=open('simple_file.txt','r')
#a=open('simple_file.txt','r')
write_file=open('simple_file_output.txt','w')
translate_string={'five':'5','one':'1','three':'3','four':'4'}
for line in read_file:
    #split will drop the end '', i.e. \n
    list_line=line.split()
    str_line=''
    for item in list_line:
        if item in translate_string:
            str_line+=translate_string[item]+' '
        else:
            str_line+=item+' '
    str_line+='\n'
    write_file.write(str_line)
write_file.close()
read_file.close()
# for i in a:
#     print(i)

