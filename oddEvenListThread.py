from threading import *;
def oddList(arr):
  total=0
  for i in range(len(arr)):
      if ((arr[i]%2)!=0):
          total=total+arr[i];
  print("sum of odd number in list:",total);         
def EvenList(arr):
    total=0
    for i in range(len(arr)):
      if ((arr[i]%2)==0):
          total=total+arr[i];
    print("sum of even number in list:",total); 

def main():
    arr=[1,2,3,4,5,6,7];
    oddlist=Thread(target=oddList,args=(arr,));
    evenlist=Thread(target=EvenList,args=(arr,));
    oddlist.start();
    evenlist.start();
   
if __name__ == "__main__":
    main();
