
def copy_binary(first_binary_file,second_binary_file):
    # open the first binary file for reading
    bfile_handle1 = open(first_binary_file, "rb")
    # open the second binary file for writing
    bfile_handle2 = open(second_binary_file, "wb")

    while True:
        # attempt to read 256 bytes each time
        buffer = bfile_handle1.read(256)

        # run out of bytes to read in,copy completed
        if len(buffer) == 0:
            break

        # copy 256 bytes to another binary file
        bfile_handle2.write(buffer)

    # close both files after processing
    bfile_handle1.close()
    bfile_handle2.close()

copy_binary('Capture.PNG','test_copy.PNG')