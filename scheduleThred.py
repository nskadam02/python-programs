from threading import *;
def printN():
    for i in range(51):
        print("s:",i);
def printReverse():
    for i in range(50,0,-1):
        print("r",i);
def main():
  threads=[];  
  thread1=Thread(target=printN);
  thread2=Thread(target=printReverse);
  thread1.start();
  thread2.start();
  threads.append(thread1);
  threads.append(thread2);
  for t in threads:
      t.join();
 

if __name__ == "__main__":
    main();
