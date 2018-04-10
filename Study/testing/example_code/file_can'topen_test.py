file_name = "input_file.txt"

try:
    file_handle = open(file_name, 'r')
except IOError:
    print("cannot open", file_name)
else:
    print(file_name, "has",
          len(file_handle.readlines()), "lines")
finally:
    print("exiting file reading")
    #file_handle.close()