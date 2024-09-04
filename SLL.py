class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
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
            self.temp=newnode
    def display(self):
        self.temp=self.head
        while self.temp!=None:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next
        print()
    def insert_at_front(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_at_end(self,data):
        newnode=node(data)
        self.temp=self.head
        while self.temp.next!=None:
            self.temp=self.temp.next
        self.temp.next=newnode
    def insert_at_mid(self,data,pos):
        newnode=node(data)
        self.temp=self.head
        i=1
        while i<pos-1:
            self.temp=self.temp.next
            i+=1
        newnode.next=self.temp.next
        self.temp.next=newnode
    def delete_at_front(self):
        temp=self.head.next
        self.head=temp
        
    def delete_at_end(self):
        self.temp=self.head
        while self.temp.next.next!=None:
            self.temp=self.temp.next
        self.temp.next=None
    def delete_at_mid(self,pos):
        self.temp=self.head
        i=1
        while i<pos-1:
            self.temp=self.temp.next
            i+=1
        temp=self.temp.next.next
        self.temp.next.next=None
        self.temp.next=temp
    def search(self):
        item = int(input("Enter an element to search:"))
        self.temp = self.head
        while self.temp:
            if self.temp.data == item:
                print(f"{item} is there")
                return
            self.temp = self.temp.next
        print(f"{item} is not there")

        
obj=SLL()
while 1:
    choice=int(input("1.create 2.display 3.insert_at_front 4.insert_at_end 5.insert_at_mid 6.detele_at_front 7.delete_at_end 8.delete_at_mid 9.search 10.exit :"))
    if choice==1:
        data=int(input("enter data:"))
        obj.create(data)
    elif choice==2:
        obj.display()
    elif choice==3:
        data=int(input("enter data:"))
        obj.insert_at_front(data)
    elif choice==4:
        data=int(input("enter data:"))
        obj.insert_at_end(data)
    elif choice==5:
        data=int(input("enter data:"))
        pos=int(input("enter position:"))
        obj.insert_at_mid(data,pos)
    elif choice==6:
        obj.delete_at_front()
    elif choice==7:
        obj.delete_at_end()
    elif choice==8:
        pos=int(input("enter position:"))
        obj.delete_at_mid(pos)
    elif choice==9:
        obj.search()
    elif choice==10:
        break
    
        
