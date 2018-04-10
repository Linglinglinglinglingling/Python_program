
def bin_to_dec(binary):
    str_binary=str(binary).strip('b')
    power=0
    sum=0
    for i in reversed(str_binary):
        sum+=int(i)*(2**power)
        power+=1
    return sum

stop=False
while stop==False:
    input_number=input('please input a number  ')
    try:
        if input_number=='q':
            stop=True

        elif input_number[0]=='b':
            try:
                print('Dec: '+str(bin_to_dec(input_number)))
            except ValueError:
                print('Error: please input the valid number')
        else:
            try:
                print('Binary: '+str(bin(int(input_number)))[2:].zfill(8))
                print('Hex: '+str(hex(int(input_number))[2:]).zfill(2))
            except ValueError:
                print('Error: please input the valid number')
    except IndexError:
        print('Error: number must not be blank')

