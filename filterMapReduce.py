from functools import *;  #module required for reduce function
def Accept():
    no=int(input("Enter the no of element in list:"));
    arr=list();
    for i in range(no):
        no1=int(input("Enter number to add in list:"));
        arr.append(no1);
    return arr;    

def Compare(no1):
  if (no1>=70 and  no1<=90):
      return True;
  else:
      return False;

def Modify(no1):
    return no1+10;

def Reduce(no1,no2):
    return no1*no2;

def main():
    RawData=Accept();
    print("Accepted data is:",RawData);
    FilterData=list(filter(Compare,RawData));
    print("Filtered data is:",FilterData);
    ModifiedData=list(map(Modify,FilterData));
    print("Modified data is:",ModifiedData);
    if(len(ModifiedData)!=0):
       Output=reduce(Reduce,ModifiedData);
       print("Final answer is:",Output);




if  __name__ == "__main__":
     main();        

