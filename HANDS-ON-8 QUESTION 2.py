class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [-1] * capacity
        self.head = 0
        self.tail = 0

    def add(self, value):
        if self.tail == self.capacity:
            print("Cannot add: Queue is full")
        else:
            self.data[self.tail] = value
            self.tail += 1

    def remove(self):
        if self.head == self.tail:
            print("Cannot remove: Queue is empty")
        else:
            element = self.data[self.head]
            self.head += 1
            return element

# Example usage
queue_capacity = int(input("Specify the queue size: "))
my_queue = MyQueue(queue_capacity)
my_queue.add(1)
my_queue.add(2)
print(my_queue.remove())
