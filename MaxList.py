def MaxList():
    no=int(input("Enter the no of element in list:"));
    arr=list();
    sumation=0;
    for i in range(no):
        no1=int(input("Enter number to add in list:"));
        arr.append(no1);
    print(arr);    
    print("Max from ist using inbuilt function:",max(arr));
    maximum=arr[0];
    for i in range(1,no):
        if(maximum<arr[i]):
            maximum=arr[i];
    print("Max from ist using for loop:",maximum);

MaxList();    
