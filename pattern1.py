def Pattern():
    num=int(input("Enter number:"));
    for i in range(num):
        for j in range(num):
            print("*",end=" ");
        print("\r")
Pattern();
