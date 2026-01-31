class DynamicArray:
    def __init__(self, cap=2):
        self.cap = cap
        self.size = 0
        self.arr = [None] * cap

    def _resize(self, new_cap):
        new_arr = [None] * new_cap
        for i in range(new_cap):
            new_arr[i] = self.arr[i]

    def size(self):
        return self.size

    def capacity(self):
        return self.cap

    def is_empty(self):
        return bool(self.size)

    def get(self, index):
        if index >= self.size or index < 0:
            raise Exception("out of range!")
        return self.arr[index]

    def set(self, index, value):
        if index > self.size or index < 0:
            raise Exception("out of range!")
        self.arr[index] = value

    def append(self, value):
        _size = self.size
        if _size == self.cap:
            self._resize(_size * 2)
        self.arr[self.size] = value
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.arr[self.size]

    def insert(self, index, value):
        _size = self.size
        if _size == self.cap:
            self._resize(_size*2)

        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i + 1]
        self.arr[index]=value
        self.size += 1

    def remove(self, index):
        for i in range(index, self.size):
            self.arr[i] = self.arr[i + 1]
        self.size -= 1

    def clear(self):
        self.size = 0

    # def destroy(self):
    #     ...

    def find(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                return i
            return -1

    def __contains__(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                return True
            return False

    def __iter__(self):
        for i in range(self.size):
            yield self.arr[i]

    def __repr__(self):
        r='Array(['
        for i in range(self.size):
            r=str(self.arr[i])+', '+r
        r=r+'])'

        return r

    def __str__(self):
        r = "["
        for i in range(self.size):
            r = str(self.arr[i]) + "," + r
        r = r + "])"

        return r

def main():
    ...

if __name__== '__main__':
    main()
