def AddList():
    no=int(input("Enter the no of element in list:"));
    arr=list();
    sumation=0;
    for i in range(no):
        no1=int(input("Enter number to add in list:"));
        arr.append(no1);
    print(arr);    
    # inbuilt function
    print("Sum of all element in list is:",sum(arr));
    # using for loop
    for i in range(no):
        sumation=sumation+arr[i];
    print("Sum using for loop is:",sumation);

AddList();    
