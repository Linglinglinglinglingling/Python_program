from stack import Stack
def check_for_balanced_parenthesis(x):
        a = Stack()
        for i in x:
            if i == '(':
                a.push(i)
            elif i == ')':
                if not (a.is_empty()):
                    a.pop()
                else:
                    return print('unmatch,extra )')
        if a.is_empty():
            print('all match')
        else:
            print("extra'('")

check_for_balanced_parenthesis('()()')