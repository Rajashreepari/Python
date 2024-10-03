class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack_LL:
    def __init__(self):
        self.top=None
    def push(self,data):
        newnode=node(data)
        newnode.next=self.top
        self.top=newnode
    def pop(self):
        if self.top ==None:
            print("Underflow")
        else:
            print(self.top.data)
            self.top=self.top.next
    def peek(self):
        print(self.top.data)
        
obj=stack_LL()
while 1:
    choice=int(input("1.push 2.pop 3.peek 4.display 5.exit"))
    if choice==1:
        data=int(input("enter data:"))
        obj.push(data)
    elif choice==2:
        obj.pop()
    elif choice==3:
        obj.peek()
    elif choice==4:
        obj.display()
    elif choice==5:
        break
    else:
        print("enter valid choice.")
