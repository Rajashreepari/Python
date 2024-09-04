class node:
    def __init__(self,co,ex):
        self.co=co
        self.ex=ex
        self.next=None
class polymerisation:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,co,ex):
        newnode=node(co,ex)
        if self.head==None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=newnode
    def display(self):
        self.temp=self.head
        while self.temp!=None:
            print(f"{self.temp.co}^{self.temp.ex} ",end=" ")
            self.temp=self.temp.next
        print()

obj=polymerisation()
while 1:
    choice=int(input("ente choice(1.create 2.display 3.exit):"))
    if choice==1:
        co=int(input("enter coefficient:"))
        ex=int(input("enter exponent:"))
        obj.create(co,ex)
    elif choice==2:
        obj.display()
    elif choice==3:
        break
