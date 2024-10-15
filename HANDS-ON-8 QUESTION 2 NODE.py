class Element:
    def __init__(self, value):
        self.value = value
        self.next_element = None

class Chain:
    def __init__(self):
        self.first = None

    def add_at_start(self, value):
        new_element = Element(value)
        new_element.next_element = self.first
        self.first = new_element

    def show(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next_element

# Example usage
my_chain = Chain()
my_chain.add_at_start(1)
my_chain.add_at_start(2)
my_chain.show()
