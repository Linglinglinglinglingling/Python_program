
class Point:
    number=0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.number+=1

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def distance_from_origin(self):
        temp_x = self.x ** 2
        temp_y = self.y ** 2
        return ((temp_x) + (temp_y)) ** 0.5

    def __eq__(self, object):
        if self.x == object.x and self.y == object.y:
            return True
        else:
            return False

    def __str__(self):
        return str(self.x) + " , " + str(self.y)

    def distance_from_given_point(self, x, y):
        distance = ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
        return distance


    def area_of_circle(self):
        import math
        radius = self.x - self.y
        area = math.pi * (radius ** 2)
        return area

    def get_number(self):
        return Point.number

    def __add__(self, another):
        return (self.x+another.x,self.y+another.y)

class Point3D:
    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z

    def distance(self):
        dis=(self.x**2+self.y**2+self.z**2)**0.5
        return dis

    def area(self):
        import math
        r=self.distance()
        a=4*math.pi*(r**2)
        return a


"""
a=Point3D(3,4,6)
print(a.get())
"""
m=Point(1,3)
b=Point(1,3)
print(b==m)
print(b)
print(m)


