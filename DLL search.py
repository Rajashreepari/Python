class node:
    def __init__(self,data):
        self.data=data
        self.pervious=None
        self.next=None
class Search:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            newnode.previous=self.temp
            self.temp=self.temp.next
    def display(self):
        print("from front:")
        self.temp=self.head
        while self.temp!=None:
            print(self.temp.data, end=" ")
            self.temp=self.temp.next
        print()
        print("reverse:")
        self.temp=self.head
        while self.temp.next!=None:
            self.temp=self.temp.next
        while self.temp!=self.head:
            print(self.temp.data,end=" ")
            self.temp=self.temp.previous
        print(self.head.data)
        print()
    def search_found(self,key):
        result=0
        self.temp=self.head
        while self.temp!=None:
            if self.temp.data==key:
                result+=1
            self.temp=self.temp.next
        if result:
            print("key found")
        else:
            print("key not found")
       
    def search_pos(self,key):
        self.temp=self.head
        i=0
        while self.temp!=None:
            i+=1
            if self.temp.data==key:
                print("key found at ",i)
            self.temp=self.temp.next

obj=Search()
while 1:
    choice=int(input("1.create 2.display 3.search _found 4.search_pos 5.exit:"))
    if choice==1:
        data=int(input("enter data:"))
        obj.create(data)
    elif choice==2:
        obj.display()
    elif choice==3:
        key=int(input("enter key to search:"))
        obj.search_found(key)
    elif choice==4:
        key=int(input("enter ket to search:"))
        obj.search_pos(key)
    elif choice==5:
        break
       
    
