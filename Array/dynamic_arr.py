class DynamicArray:
    def __init__(self, cap=2):
        self.cap = cap
        self.size = 0
        self.arr = [None] * cap

    def _resize(self, new_cap):
        new_arr = [None] * new_cap
        for i in range(self.cap):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.cap = new_cap

    def size(self):
        return self.size

    def capacity(self):
        return self.cap

    def is_empty(self):
        return self.size == 0

    def get(self, index):
        if index >= self.size or index < 0:
            raise Exception("out of range!")
        return self.arr[index]

    def set(self, index, value):
        if index >= self.size or index < 0:
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

        for i in range(self.size, index-1, -1):
            self.arr[i+1] = self.arr[i]

        self.arr[index]=value
        self.size += 1

    def remove(self, index):
        for i in range(index, self.size):
            self.arr[i] = self.arr[i + 1]
        self.size -= 1

    def clear(self):
        self.size = 0

    def destroy(self):
        self.arr = []
        self.size = 0
        self.cap = 0

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

    def __len__(self):
        return self.size

    def __repr__(self):
        r='Array(['
        for i in range(self.size):
            r+=str(self.arr[i])+','
        r=r.rstrip(',')+'])'
        return r

    def __str__(self):
        r='['
        for i in range(self.size):
            r+=str(self.arr[i])+','
        r=r.rstrip(',')+']'
        return r

def main():
    da=DynamicArray()
    da.append(10)
    da.append(20)
    da.append(30)
    da.append(40)
    da.append(50)
    print('initial array:', da)
    print('length:',len(da))
    print('insert 9 at index 2:',end=' ')
    da.insert(2,9)
    print(da)
    print('get index 2:',end=' ')
    print(da.get(2))
    print('remove index 3:')
    da.remove(3)
    print('insert at index 0:',end=' ')
    da.set(0,100)
    print(da)
    print("delete last:", da.pop())
    print("length after pop:", len(da))
    print(da)
    print("find 10:", da.find(10))
    print("find 40:", da.find(40))
    print('is empty?:',da.is_empty())
    da.clear()
    print('after clear:')
    print('is empty?:',da.is_empty())
    # print(100 in da)
    # print(20 in da)
    # print('clean:',end=' ')
    # da.clear()
    # print(len(da))
    # print(da)

if __name__== '__main__':
    main()
