def pattern():
    num=int(input("Enter number:"));
    for i in range(num,0,-1):
        for i in range(1,i+1):
            print("*",end=" ");
        print("\r");

pattern();            
