
#include <iostream>

class ResizableArray {
private:
    int *elements;
    int capacity;
    int currentSize;

public:
    ResizableArray() : elements(nullptr), capacity(0), currentSize(0) {}

    ~ResizableArray() {
        delete[] elements;
    }

    void add(int value) {
        if (currentSize >= capacity) {
            int newCapacity = (capacity == 0) ? 1 : capacity * 2;
            int *temp = new int[newCapacity];
            for (int i = 0; i < currentSize; ++i) {
                temp[i] = elements[i];
            }
            delete[] elements;
            elements = temp;
            capacity = newCapacity;
        }
        elements[currentSize++] = value;
    }

    int get(int index) const {
        if (index < 0 || index >= currentSize) {
            std::cerr << "Error: index out of bounds\n";
            exit(EXIT_FAILURE);
        }
        return elements[index];
    }

    int& operator[](int index) {
        if (index < 0 || index >= currentSize) {
            std::cerr << "Error: index out of bounds\n";
            exit(EXIT_FAILURE);
        }
        return elements[index];
    }

    int size() const {
        return currentSize;
    }
};

int main() {
    ResizableArray arr;
    for (int i = 0; i < 10; ++i) {
        arr.add(i);
    }
    for (int i = 0; i < arr.size(); ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
