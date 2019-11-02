def Pattern():
    num=int(input("Enter number"));
    for i in range(num+1):
        for i in range(1,i+1):
            print(i,end=" ");
        print("\r");

Pattern();       
