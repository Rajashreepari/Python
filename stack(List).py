class stack_list:
    def __init__(self,size):
        self.stack=[]
        self.max=size
        self.top=-1
    def display(self):
        for i in range(0,len(self.stack)):
              print(self.stack[i],end=" ")
        print()
    def push(self,item):
        if len(self.stack)<self.max:
            self.stack.append(item)
            print("pushed item:",item)
            self.top+=1
        else:
            print("Stack OVERFLOW.")
    def pop(self):
        if len(self.stack)!=-1:
            poped_data=self.stack.pop()
            print("Poped item:",poped_data)
            self.top-=1
        else:
            print("stack UNDERFLOW.")
    def peek(self):
        print("The peek item in stack:",self.stack[self.top])
        
size=int(input("enter size of the array:"))
Stack=stack_list(size)
print("1.display 2.push 3.pop 4.peek 5.Exit")
while 1:
    choice=int(input("enter your choice:"))
    if choice==1:
        Stack.display()
    elif choice==2:
        item=int(input("enter item:"))
        Stack.push(item)
    elif choice==3:
        Stack.pop()
    elif choice==4:
        Stack.peek()
    elif choice==5:
        break
    
