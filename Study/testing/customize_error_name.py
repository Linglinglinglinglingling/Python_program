#if self, module name is __main__
#if import, module name is the name of the imported module
class NotAgoodinput(Exception):
    pass
def list_multiplication(list_1,list_2):
    len_1=len(list_1)
    len_2=len(list_2)
    if len_1!=len_2:
        raise NotAgoodinput ('my error')
    result_list=[]
    for item_1 in list_1:
        new_list=[]
        for item_2 in list_2:
            new_list.append(item_1*item_2)
        result_list.append(new_list)
    return result_list


a=[2,3,4,5]
b=[4,5,6]
c=list_multiplication(a,b)
print(c)
