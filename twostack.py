class TwoStacks:
    def __init__(self, size=1000):
        self.size = size
        self.array = [None] * size
        self.top1 = -1   # Top of stack 1
        self.top2 = size  # Top of stack 2, initialized to end of array

    def push1(self, value):
        if self.top1 + 1 < self.top2:
            self.top1 += 1
            self.array[self.top1] = value
        else:
            print("Stack overflow. push from stack 1 failed.")

    def push2(self, value):
        if self.top2 - 1 > self.top1:
            self.top2 -= 1
            self.array[self.top2] = value
        else:
            print("Stack overflow. push from stack 2 failed.")

    def pop1(self):
        if self.top1 >= 0:
            value = self.array[self.top1]
            self.top1 -= 1
            return value
        else:
            print("Stack underflow. pop from stack 1 failed")
            return None

    def pop2(self):
        if self.top2 < self.size:
            value = self.array[self.top2]
            self.top2 += 1
            return value
        else:
            print("Stack underflow. pop from stack 2 failed")
            return None

    def print_stack1(self):
        if self.top1 == -1:
            print("Stack 1 Elements:")
            
        else:
            print("Stack 1 Elements:")
            for i in range(self.top1, -1, -1):
                print(self.array[i], end=" ")
        print()    

    def print_stack2(self):
        if self.top2 == self.size:
            print("Stack 2 Elements:")
            
        else:
            print("Stack 2 Elements:")
            for i in range(self.top2, self.size):
                print(self.array[i], end=" ")
        print()
            



ts = TwoStacks()

n1 = int(input())
elements_stack1 = list(map(int, input().split()))
for element in elements_stack1:
  ts.push1(element)

n2 = int(input())
elements_stack2 = list(map(int, input().split()))
for element in elements_stack2:
  ts.push2(element)
  
ts.print_stack1()

ts.print_stack2()

n1_delete = int(input())
for _ in range(n1_delete):
  ts.pop1()
n2_delete = int(input())
for _ in range(n2_delete):
  ts.pop2()

ts.print_stack1()
ts.print_stack2()


