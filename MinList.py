def MinList():
    no=int(input("Enter the no of element in list:"));
    arr=list();
    sumation=0;
    for i in range(no):
        no1=int(input("Enter number to add in list:"));
        arr.append(no1);
    print(arr);    
    print("Min from ist using inbuilt function:",min(arr));
    minimum=arr[0];
    for i in range(1,no):
        if(minimum>arr[i]):
            minimum=arr[i];
    print("Min from ist using for loop:",minimum);

MinList();    
