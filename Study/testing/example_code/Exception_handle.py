try:
    # open simple_file.txt for reading
    input_handle = open('simple_file1.txt', 'r')

    # open output_file.txt for writing
    output_handle = open('output_file.txt', 'w')

except IOError:
    print("cannot open files")

except RuntimeError:
    print("some run-time errors")

else:
    # perform some data processing
    for line in input_handle:
        line = line.strip("\n")
        line_tokens = line.split(" ")

        if line_tokens[2] == "one":
            line_tokens[2] = '1'
        elif line_tokens[2] == "two":
            line_tokens[2] = '2'
        elif line_tokens[2] == "three":
            line_tokens[2] = '3'
        elif line_tokens[2] == "four":
            line_tokens[2] = '4'
        elif line_tokens[2] == "five":
            line_tokens[2] = '5'

        new_line = line_tokens[0] + " " + line_tokens[1] + " " + line_tokens[2] + "\n"
        output_handle.write(new_line)

    # close both files after processing
    input_handle.close()
    output_handle.close()

finally:
    print("Exiting program...")