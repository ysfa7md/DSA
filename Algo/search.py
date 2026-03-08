class Search:
    @staticmethod
    def binary_search(arr, value, start, end):
        if start > end:
            return -1

        mid = (start + end) // 2

        if arr[mid] == value:
            return mid

        if value > arr[mid]:
            return Search.binary_search(arr, value, mid + 1, end)
        else:
            return Search.binary_search(arr, value, start, mid - 1)

    @staticmethod
    def linear_search(arr, value):
        for i in range(len(arr)):
            if arr[i] == value:
                return i
        return -1


def main():
    arr=[1,2,3,4,5,6,7,8,9,10]
    value=7
    start=0
    end=len(arr)

    res1= Search.binary_search(arr, value, start, end)

    print(f"Value {value} found at index {res1}")
    print('$'*30)
    
    print(f"Value {2} found at index {Search.linear_search(arr, 1)}")
    print(f"Value {7} found at index {Search.linear_search(arr, 7)}")

if __name__=='__main__':
    main()
