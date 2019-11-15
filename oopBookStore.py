class BookStore:
    # class variable
    NoOfBooks=0; 
    def __init__(self,name,author):
        self.bookName=name;
        self.authorName=author;
        BookStore.NoOfBooks=BookStore.NoOfBooks+1;
    def Display(self):
        print("Book name is:",self.bookName);
        print("Author name is:",self.authorName);
        print("Total books are:",BookStore.NoOfBooks);

def main():
    obj1=BookStore('C programming','Dennis Ritchie');
    obj1.Display();
    obj2=BookStore('Modern OS','Achyut Godbole'); 
    obj2.Display();


if __name__ == "__main__":
    main();                
