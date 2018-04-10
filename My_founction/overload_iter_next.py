class a:
    def __init__(self,x):
        self.x=x
        self.list=[1,2,3,4,5]

    def mutator(self,y):
        self.x+=y

    def __str__(self):
        return str(self.x)

    def __next__(self):
        if self.iter>=len(self.list):
            raise StopIteration
        item=self.list[self.iter]
        self.iter+=1
        return item

    def __iter__(self):
        self.iter=0
        return self


def b(object):
    return object.mutator(1)

x=a(5)
c=iter(x)
print(x is c)

for i in x:
    print(i)
print(x.list)
print(x.iter)
