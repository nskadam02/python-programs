from functools import *;  #module required for reduce function
def Accept():
    no=int(input("Enter the no of element in list:"));
    arr=list();
    for i in range(no):
        no1=int(input("Enter number to add in list:"));
        arr.append(no1);
    return arr;

def main():
    RawData=Accept();
    print("Accepted data is:",RawData);
    FilterData=list(filter(lambda no1:not(no1%2),RawData));
    print("Filtered data is:",FilterData);
    ModifiedData=list(map(lambda no1:(no1**2),FilterData));
    print("Modified data is:",ModifiedData);
    if(len(ModifiedData)!=0):
       Output=reduce(lambda no1,no2:no1+no2,ModifiedData);
       print("Final answer is:",Output);

if __name__ == "__main__":
    main();    
