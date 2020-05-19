import ctypes

class DynamicArray:

    def __init__(self):
        self.current_size = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.current_size

    def __getitem__(self, k):
        if not 0 <= k < self.current_size:
            return IndexError("Index is out of bounds")

        return self.array[k]

    def append(self, element):
        if self.current_size == self.capacity:
            self.capacity = 2 * self.capacity
            self._resize(self.capacity)
        
        self.array[self.current_size] = element
        self.current_size += 1

    def _resize(self, new_cap):
        new_arr = self.make_array(new_cap)
        for i in range(self.current_size):
            new_arr[i] = self.array[i]

        self.array = new_arr

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def print_array(self):
        for i in range(self.current_size):
            print(self.array[i])

if __name__ == "__main__":
    array = DynamicArray()
    array.append(1)
    array.append(2)
    array.append(3)
    print(array.__getitem__(2))
    array.print_array()
    print(len(array))
    print(array[0])
    