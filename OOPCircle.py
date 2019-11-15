class Circle:
    PI=3.14;
    def __init__(self):
        self.radius=0.0;
        self.area=0.0;
        self.circumference=0.0;

    def Accept(self):
        self.radius=float(input("Enter radius")); 
    def Area(self):
        self.area=self.PI*self.radius*self.radius;
    def Circum(self):
        self.circumference=2*self.PI*self.radius;    
    def Display(self):
        print("radius is:",self.radius);
        print("Area is:",self.area);
        print("circumference:",self.circumference);       




def main():
    obj1=Circle();
    obj1.Accept();
    obj1.Area();
    obj1.Circum();
    obj1.Display();
    print("second object");
    obj2=Circle();
    obj2.Accept();
    obj2.Area();
    obj2.Circum();
    obj2.Display();

if __name__ == "__main__":
    main();
