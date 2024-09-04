# Team no:8
# Name: RAJASHREE P (Roll no:23110037)
#1.Write a  Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class circle:
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        area=self.radius**2
        print("Area of a circle with radius",self.radius,":",area)
    def Perimeter(self):
        perimeter=2*3.14*self.radius
        print("Perimeter of a Circle with radius",self.radius,":",perimeter)
    def Area_and_Perimeter(self,radius):
        area=self.radius**2
        perimeter=2*3.14*self.radius
        print("Area of a circle with radius",self.radius,":",area)
        print("Perimeter of a Circle with radius",self.radius,":",perimeter)

choice=int(input("1.Area 2.Perimeter 3.Both"))
radius1=float(input("Enter radius:"))
circle1=circle(radius1)
if choice==1:
   circle1.Area()
elif choice==2:
   circle1.Perimeter()
elif choice==3:
    circle1.Area_and_Perimeter()
    
    
