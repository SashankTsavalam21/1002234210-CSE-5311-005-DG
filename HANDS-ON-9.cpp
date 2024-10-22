#include <iostream>
#include <cmath>

struct Entry {
    int k;
    int v;
    Entry* n;
    Entry* p;
    Entry(int key, int value) : k(key), v(value), n(nullptr), p(nullptr) {}
};

class HashMap {
private:
    Entry** storage;
    int capacity;
    int count;
    const float maxLoad = 0.75f;
    const float minLoad = 0.25f;
    int (*hashFunc)(int, int);

    static int defaultHash(int key, int size) {
        const float constant = 0.6180339887f;
        float fractional = (key * constant) - floor(key * constant);
        return floor(size * fractional);
    }

    void reallocate(int newCap) {
        Entry** newStorage = new Entry*[newCap];
        for (int i = 0; i < newCap; ++i) {
            newStorage[i] = nullptr;
        }
        for (int i = 0; i < capacity; ++i) {
            Entry* current = storage[i];
            while (current != nullptr) {
                Entry* next = current->n;
                int index = hashFunc(current->k, newCap);
                current->n = newStorage[index];
                if (newStorage[index] != nullptr)
                    newStorage[index]->p = current;
                newStorage[index] = current;
                current->p = nullptr;
                current = next;
            }
        }
        delete[] storage;
        storage = newStorage;
        capacity = newCap;
    }

public:
    HashMap(int (*customHashFunc)(int, int) = defaultHash)
        : capacity(8), count(0), hashFunc(customHashFunc) {
        storage = new Entry*[capacity]();
    }

    ~HashMap() {
        for (int i = 0; i < capacity; ++i) {
            Entry* current = storage[i];
            while (current != nullptr) {
                Entry* next = current->n;
                delete current;
                current = next;
            }
        }
        delete[] storage;
    }

    void insert(int key, int value) {
        if (count >= maxLoad * capacity)
            reallocate(2 * capacity);

        int index = hashFunc(key, capacity);
        Entry* newEntry = new Entry(key, value);
        if (storage[index] != nullptr) {
            newEntry->n = storage[index];
            storage[index]->p = newEntry;
        }
        storage[index] = newEntry;
        count++;
    }

    void remove(int key) {
        int index = hashFunc(key, capacity);
        Entry* current = storage[index];
        while (current != nullptr) {
            if (current->k == key) {
                if (current->p != nullptr)
                    current->p->n = current->n;
                else
                    storage[index] = current->n;
                if (current->n != nullptr)
                    current->n->p = current->p;
                delete current;
                count--;
                break;
            }
            current = current->n;
        }

        if (count <= minLoad * capacity && capacity > 8)
            reallocate(capacity / 2);
    }

    int search(int key) {
        int index = hashFunc(key, capacity);
        Entry* current = storage[index];
        while (current != nullptr) {
            if (current->k == key)
                return current->v;
            current = current->n;
        }
        return -1;
    }
};

int main() {
    HashMap map;
    map.insert(5, 100);
    map.insert(15, 200);
    map.insert(25, 300);

    std::cout << "Value for key 5: " << map.search(5) << std::endl;
    std::cout << "Value for key 15: " << map.search(15) << std::endl;
    std::cout << "Value for key 25: " << map.search(25) << std::endl;

    map.remove(15);

    std::cout << "Value for key 15 after removal: " << map.search(15) << std::endl;

    return 0;
}
