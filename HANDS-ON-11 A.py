
class ExpandableArray:
    def __init__(self):
        self.initial_capacity = 1
        self.items = [None] * self.initial_capacity
        self.current_count = 0

    def add_item(self, value):
        if self.current_count == self.initial_capacity:
            self.expand_capacity(self.initial_capacity * 2)
        self.items[self.current_count] = value
        self.current_count += 1

    def expand_capacity(self, new_capacity):
        updated_items = [None] * new_capacity
        for idx in range(self.current_count):
            updated_items[idx] = self.items[idx]
        self.items = updated_items
        self.initial_capacity = new_capacity

    def calculate_amortized_runtime(self, steps):
        total_operations = 0
        for _ in range(steps):
            if self.current_count == self.initial_capacity:
                total_operations += self.initial_capacity
                self.expand_capacity(self.initial_capacity * 2)
            total_operations += 1
            self.current_count += 1
        return total_operations / steps

expandable_array = ExpandableArray()
steps = 100
amortized_runtime = expandable_array.calculate_amortized_runtime(steps)

print("Average amortized runtime per operation:", amortized_runtime)
