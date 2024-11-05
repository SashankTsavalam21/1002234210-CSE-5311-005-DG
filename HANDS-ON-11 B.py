class ResizableList:
    def __init__(self):
        self.capacity = 1
        self.items = [None] * self.capacity
        self.count = 0

    def add(self, value):
        if self.count == self.capacity:
            self.expand(self.capacity * 2)
        self.items[self.count] = value
        self.count += 1

    def expand(self, new_capacity):
        updated_items = [None] * new_capacity
        for index in range(self.count):
            updated_items[index] = self.items[index]
        self.items = updated_items
        self.capacity = new_capacity

    def amortized_cost_accounting(self, operations):
        cumulative_cost = 0
        for _ in range(operations):
            if self.count == self.capacity:
                cumulative_cost += self.capacity
                self.expand(self.capacity * 2)
            cumulative_cost += 2
            self.count += 1
        return cumulative_cost / operations

resizable_list = ResizableList()
operation_count = 1000
average_amortized_cost = resizable_list.amortized_cost_accounting(operation_count)

print("Average amortized runtime with accounting approach:", average_amortized_cost)
