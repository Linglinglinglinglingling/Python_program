file_handle=open('test_file.txt','r')
# create a list to hold each line
list_of_lines = []

# read one line at a time and append it to the list
for line in file_handle:
    list_of_lines.append(line.strip())

print(list_of_lines)