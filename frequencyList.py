def FrequencyList():
    no=int(input("Enter the no of element in list:"));
    arr=list();
    sumation=0;
    for i in range(no):
        no1=int(input("Enter number to add in list:"));
        arr.append(no1);
    print(arr);    
    no2=int(input("Enter the number to find the frequency:"));
    print("frquency of",no2,"in list using inbuilt:",arr.count(no2));
    freq=0;
    for i in range(no):
        if(arr[i]==no2):
            freq=freq+1;

    print("frquency of",no2,"in list using loop:",freq);        
FrequencyList();
