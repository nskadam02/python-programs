from threading import *;
def Capital(str1):
    print("thrad name of capital:",current_thread().name)
    print("thread id of Capital:",get_ident());

    for i in range(len(str1)):
        if str1[i].isupper():
            print("capital",str1[i]);

def Small(str1):
    print("thrad name of Small:",current_thread().name)
    print("thread id of Small:",get_ident());
  
    for i in range(len(str1)):
        if str1[i].islower():
            print("small",str1[i]);

def Digits(str1):
    print("thrad name digits:",current_thread().name)
    print("thread id digit:",get_ident());
    for i in range(len(str1)):
        if str1[i].isdigit():
            print("digit",str1[i]);

def main():
   str1="MynameIs12g";
   print("string is:",str1);
   small=Thread(target=Small,args=(str1,));
   big=Thread(target=Capital,args=(str1,));
   digit=Thread(target=Digits,args=(str1,));
   small.start();
   big.start();
   digit.start();

if __name__=="__main__":
    main();        
