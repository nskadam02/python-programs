class Demo:
    value=10;
    def __init__(self,no1,no2):
      # num1 and num2 are instance variable
      self.num1=no1;
      self.num2=no2;
    def Fun(self):
        print("first instance variable:",self.num1);
    def Gun(self):
         print("second instance variable:",self.num2);    


def main():
    obj1=Demo(10,20);
    obj1.Fun();
    obj1.Gun();
    print("second object");
    obj2=Demo(40,50);
    obj2.Fun();
    obj2.Gun();
if __name__ == "__main__":
   main();
