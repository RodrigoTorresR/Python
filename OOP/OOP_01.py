import math
#Creating Python Classes
class MyFirstClass:
    pass
"""
    >>> a = MyFirstClass()
    >>> b = MyFirstClass()
    >>> print (a)
    <__main__.MyFirtsClass object at 0xb7b7faec>
    >>> print (b)
    <__main__.MyFirtsClass object at 0xb7b7fbac>
    >>>
"""
#Adding Attributes
class Point:
    pass
p1=Point()
p2=Point()
#A
p1.x=5 
p1.y=4

p2.x=3
p2.y=6
#B
print(p1.x, p1.y)
print(p2.x, p2.y)
"""
    Adding attributes as A or B above
    is discoraged, because breaks the OOP
    principles, actions like those are
    permited in Python but they are a bad
    programming practices
"""
print('####END EXAMPLE####')
class PointM:
    def reset (self):
        self.x = 0
        self.y = 0
p = PointM()
p.reset()
print(p.x, p.y)
"""
    Adding attributes requires the use of self Method
    this method is an prametter of the class definition too
    represents a high superior class used by our class
    in OOP we called parent class
    if we forgot to put the Self parameter Python gives the
    next message:
    >>>p=point()
    >>>p.reset()
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: reset () takes no arguments (1 given)
    That causes the error is:
    Class PointM:
        def reset(): #we don´t put the Self parameter
            pass
"""
print('####END EXAMPLE####')
#import math #this line goes at the benning of the code
class PointMore:
    def move(self, x, y):
        self.x=x
        self.y=y
    def reset(self):
        self.move(0,0) #We called a function already defined
    def calculate_distance(self, other_point): #To refer to another object we can use other or any word
        return math.sqrt(
                (self.x - other_point.x)**2 +
                (self.y - other_point.y)**2)
#How to use it:
point1= PointMore()
point2= PointMore()

point1.reset()
point2.move(5,0)
print(point2.calculate_distance(point1))
assert(point2.calculate_distance(point1) == 
       point1.calculate_distance(point2))
point1.move(3,4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))
"""
   Only added a new function to the class and remarks the use of the word self, as the another parameter 
"""
print('####END EXAMPLE####')
class PointC:                 #Class with a "COSNTRUCTOR"
    def __init__(self, x, y): #Special method made a function like a "CONSTRUCTOR" in another languajes
        self.move(x,y)
    def move(self, x, y):
        self.x=x
        self.y=y
    def reset(self):
        self.move(0,0)
#Constructing a Point
point = PointC(3,5)
print(point.x, point.y)
"""
    Using a contructor function is more according to an OOP methodology, until now we were usign
    Pythons featrures to create Objects, it's possible but is a bad programming practice 
"""
print('####END EXAMPLE####')
class PointConstructorDefaults:     #Class with a "COSNTRUCTOR" and Defaults Arguments
    def __init__(self, x=0, y=0): #Special method made a function like a "CONSTRUCTOR" in another languajes
        self.move(x,y)
    def move(self, x, y):
        self.x=x
        self.y=y
    def reset(self):
        self.move(0,0)
#Constructing a Point
pointA = PointConstructorDefaults(3,5)
pointB = PointConstructorDefaults() #We don't provide any arguments, Creates an Object with the Default values
print(pointA.x, pointA.y, "Values provides before during the creation of the Object") 
print(pointB.x, pointB.y, 
      "Defautl Values, we don't specifies any value at the creation of the Object") #Show the object with 
                                                                                    #a "Default" values
"""
    Usually the constructor has some Defaults arguments in order to avoid create "empty" Objects
    this could lead to a errors in the code.
"""
print('####END EXAMPLE####')
#import math #this sentence goes at the beginning of the file
class PointH:       #We use the H postfix to inidicates Help to differentiate this class from the other Point class 
    'Represents a point in two-dimensional gemoetric coordinates'

    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point. The x and y cooridnates can be specified.
           If they are not, the poin defaults to the origins.
        '''
        self.move(x,y)
    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x=x
        self.y=y
    def reset(self):
        'reset the poin back to the geometric origin: 0, 0'
        self.move(0, 0)
    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second point passed as a parameter.
           This function uses the Pythagorean Theorem to calculate the distance between the two points.
           The distance is returned as a float.
        """
        return math.sqrt(
                (self.x - other_point.x)**2+
                (self.y - other_point.y)**2)

