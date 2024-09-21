class GenericMinHeap:
    def __init__(self):
        self.heaparray = []

    def _parent(self, index):
        return (index - 1) >> 1

    def _left_child(self, index):
        return (index << 1) + 1

    def _right_child(self, index):
        return (index << 1) + 2

    def _heapify(self, index):
        size = len(self.heaparray)
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < size and self.heaparray[left] < self.heaparray[smallest]:
            smallest = left
        if right < size and self.heaparray[right] < self.heaparray[smallest]:
            smallest = right

        if smallest != index:
            self.heaparray[index], self.heaparray[smallest] = self.heaparray[smallest], self.heaparray[index]
            self._heapify(smallest)

    def build_min_heap(self, elements):
        self.heaparray = elements[:]
        for i in range((len(self.heaparray) - 1) >> 1, -1, -1):
            self._heapify(i)

    def insert(self, value):
        self.heaparray.append(value)
        index = len(self.heaparray) - 1
        while index > 0 and self.heaparray[self._parent(index)] > self.heaparray[index]:
            parent_idx = self._parent(index)
            self.heaparray[parent_idx], self.heaparray[index] = self.heaparray[index], self.heaparray[parent_idx]
            index = parent_idx

    def pop_root(self):
        if not self.heaparray:
            return None
        root = self.heaparray[0]
        last_element = self.heaparray.pop()
        if self.heaparray:
            self.heaparray[0] = last_element
            self._heapify(0)
        return root

if __name__ == "__main__":
    min_heap = GenericMinHeap()

    print("Enter an array:")
    arr = list(map(int, input().split(" ")))
    min_heap.build_min_heap(arr)
    print("Initial Heap array: ", min_heap.heaparray)

    min_heap.insert(2)
    print("Heap array: ", min_heap.heaparray)

    root = min_heap.pop_root()
    print("Removed node from heap:", root)
    print("Heap array: ", min_heap.heaparray)

    root = min_heap.pop_root()
    print("Removed node from heap:", root)
    print("Heap array: ", min_heap.heaparray)
