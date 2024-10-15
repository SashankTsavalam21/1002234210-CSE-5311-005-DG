class MyStack:
    def __init__(self, max_capacity):
        self.capacity = max_capacity
        self.container = [-1] * max_capacity
        self.pointer = -1

    def insert(self, value):
        if self.pointer >= self.capacity - 1:
            print("Cannot insert: Stack is full")
        else:
            self.pointer += 1
            self.container[self.pointer] = value

    def remove(self):
        if self.pointer == -1:
            print("Cannot remove: Stack is empty")
        else:
            element = self.container[self.pointer]
            self.pointer -= 1
            return element

# Example usage
stack_size = int(input("Define the stack size: "))
my_stack = MyStack(stack_size)
my_stack.insert(1)
my_stack.insert(2)
print(my_stack.remove())
