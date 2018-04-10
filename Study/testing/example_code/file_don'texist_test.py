file_name = "input_file2.txt"

try:
    file_handle = open(file_name, 'r')
except FileNotFoundError:
    print("cannot open", file_name)
else:
    print(file_name, "has",
          len(file_handle.readlines()), "lines")
    file_handle.close()
finally:
    print("exiting file reading")
    # file_handle.close()