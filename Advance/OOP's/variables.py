# variables
# -Static  
# -instance(object dependent variable )those variables which are changing the value as we change the object
# -local
class Students:
    def __init__(self, name, marks):
        self.x = name # instance variable
        self.y = marks # instance variable
obj=Students("Anushka",5)
print(obj.x)
print(obj.y)