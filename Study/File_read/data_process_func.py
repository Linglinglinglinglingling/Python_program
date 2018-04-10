def data_preprocessing(input_file, output_file):
    # open input_file for reading
    input_handle = open(input_file, 'r')

    # open output_file for writing
    output_handle = open(output_file, 'a')

    for line in input_handle:
        # perform some data processing (e.g. convert to lowercases)
        line = line.lower()
        output_handle.write(line)

    # close both files after processing
    print(1)
    for line in input_handle:
        print(line)
    input_handle.close()
    output_handle.close()

data_preprocessing('test_file.txt','test_file_output.txt')