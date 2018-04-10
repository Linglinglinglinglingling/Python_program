def a(*x):
    result=0
    for i in x:
        result+=i
    return result

print(123)

def main():
    print(a(1,2,3,4))

if __name__ == '__main__':
    main()