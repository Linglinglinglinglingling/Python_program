class a:
    def __init__(self,x):
        self.x=x

    def mutator(self,y):
        self.x+=y

    def __str__(self):
        return str(self.x)

def b(object):
    return object.mutator(1)

x=a(5)
b(x)
print(x)