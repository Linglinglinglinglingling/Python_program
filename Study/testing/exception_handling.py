a=100
try:
    a+=1
    a=1/0
except:
    print("can't devide by zero")
else:
    print('it is working')

finally:
    print('end')
    print(a)