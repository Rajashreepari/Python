class node:
    def __init__(self,data):
        self.data=data
        self.pervious=None
        self.next=None
class CLL_doubly:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            self.temp=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.previous=self.tail
            newnode.next=self.head
            self.head.previous=newnode
            self.tail=newnode      
    def display(self):
        self.temp=self.head
        while self.temp.next!=self.head:
            print(self.temp.data, end=" ")
            self.temp=self.temp.next
        print(self.tail.data)
    def insert_at_front(self,data):
        newnode=node(data)
        newnode.next=self.head
        newnode.previous=self.tail
        self.tail.next=newnode
        self.head=newnode
    def insert_at_end(self,data):
        newnode=node(data)
        self.tail.next=newnode
        newnode.previous=self.tail
        self.tail=newnode
        newnode.next=self.head
        self.head.previous=newnode
    def insert_at_mid(self,data,pos):
        newnode=node(data)
        self.temp=self.head
        i=1
        while i<pos-1:
            self.temp=self.temp.next
            i+=1
        newnode.previous=self.temp
        newnode.next=self.temp.next
        temp=self.temp.next
        self.temp.next=newnode
        temp.previous=newnode
    def delete_at_front(self):
        self.head=self.head.next
        self.head.previous=self.tail
        self.tail.next=self.head
    def delete_at_end(self):
        self.temp=self.head
        while self.temp.next.next!=self.head:
            self.temp=self.temp.next
        self.temp.next.next=None
        self.temp.next=self.head
        self.head.previous=self.temp
        self.tail=self.temp
    def delete_at_mid(self,pos):
        self.temp=self.head
        i=1
        while i<pos-1:
            self.temp=self.temp.next
            i+=1
        temp=self.temp.next.next
        self.temp.next.next=None
        self.temp.next=temp
        

obj=CLL_doubly()
while 1:
    choice=int(input("1.create 2.display 3.insert_at_front 4.insert_at_end 5.insert_at_mid 6.delete_at_front 7.delete_at_end 8.delete_at_mid 9.exit :"))
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
        pos=int(input("enter position to delete:"))
        obj.delete_at_mid(pos)
    elif choice==9:
        break
        
        
        
