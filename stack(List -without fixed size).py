class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack Underflow!"
        return  self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is Empty!"
        return  self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        return self.stack


obj = Stack()
while True:
    print("1.Push\n2.Pop\n3.Peek\n4.Show Size\n5.Display\n6.Exit")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        data = int(input("Enter data: "))
        obj.push(data)
    elif choice == 2:
        print("Popped :",obj.pop())
    elif choice == 3:
        print("peeked :",obj.peek())
    elif choice == 4:
        print(obj.size())
    elif choice == 5:
        print(obj.display())
    elif choice == 6:
        break
    else:
        print("Invalid Choice")
