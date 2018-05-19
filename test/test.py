def input_validation(string):
    try:
        if "t=" in string and "d=" not in string:
            return False
        if "d=" in string and "t=" not in string:
            return False
        argument_list=string.strip().split()

        for item in argument_list:
            if "t=" in item or "d=" in item:
                if int(item[2:])<=0:
                    print("please input the valid number" + "\n")
                    return False
            elif item not in ["1","2","3","4","q"]:
                    print("please input the valid number" + "\n")
                    return False
        return True
    except:
        print("please input the valid number" + "\n")
        return False

a="1 t=10"
print(input_validation(a))