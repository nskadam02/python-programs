class Arithmetic:
    def __init__(self):
        self.value1=0;
        self.value2=0;
    def Accept(self):
        self.value1=float(input("Enter first number:"));
        self.value2=float(input("Enter second number:"));
    def Addition(self):
        return self.value1+self.value2;
    def Substraction(self):
        return self.value1-self.value2;
    def Multiply(self):
        return self.value1*self.value2;
    def Division(self):
        return self.value1//self.value2;                
def main():
    obj1=Arithmetic();
    obj1.Accept();
    print("Addition is:",obj1.Addition());
    print("Substraction is:",obj1.Substraction());
    print("Multiplication is:",obj1.Multiply());
    print("Division is:",obj1.Division());


if __name__ == "__main__":
    main();    
