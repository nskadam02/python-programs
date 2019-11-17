from threading import *;  #necessary for making thread
from os import *;  #necessary for getting pid and ppid

def Even():
  print("pid of Even:",getpid());
  print("ppid of Even",getppid());  
  no=10;
  cnt=1;
  while cnt<=no:
      print("Even number:",cnt*2);
      cnt=cnt+1;


def Odd():
   print("pid of Odd:",getpid());
   print("ppid of Odd",getppid());  
   no=10;
   cnt=0;
   while cnt<=no:
       print("Odd number",(cnt*2)+1);
       cnt=cnt+1;
       

def main():
    print("pid of main:",getpid());
    print("ppid of main",getppid());
    odd=Thread(target=Odd);
    even=Thread(target=Even);
    odd.start();
    even.start();

if __name__ == "__main__":
    main();
