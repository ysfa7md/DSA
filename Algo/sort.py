class Sort:
    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i
            while j > 0 and arr[j - 1] > key:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = key

    # def insertion_sort(arr):
    #     for j in range(1,len(arr),1):
    #         key=arr[j]
    #         i=j-1
    #         while arr[i]>key and i >=0:
    #             arr[i+1]=arr[i]
    #             i-=1
    #         arr[i+1]=key

    @staticmethod
    def selection_sort(arr):
        n = len(arr)

        for i in range(n):
            min_idx = i
            for j in range(i, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[min_idx], arr[i] = arr[i], arr[min_idx]

    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        swaped = True

        while swaped:
            swaped = False
            for i in range(n - 1):
                if arr[i + 1] < arr[i]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swaped = True
                    n = i + 1
            # n-=1

    @staticmethod
    def merg(arr, start, mid, end):
        i = 0
        j = 0
        left = arr[start : mid + 1]
        right = arr[mid + 1 : end + 1]

        len_left = len(left)
        len_right = len(right)

        while i < len_left and j < len_right:
            if left[i] < right[j]:
                arr[start + i + j] = left[i]
                i += 1
            else:
                arr[start + i + j] = right[j]
                j += 1
        curr_idx = start + i + j

        if i < len_left:
            arr[curr_idx : curr_idx + len(left[i:])] = left[i:]
        if j < len_right:
            arr[curr_idx : curr_idx + len(right[j:])] = right[j:]

    @staticmethod
    def merg_sort(arr, start, end):
        if start < end:
            mid = start + (end - start) // 2
            Sort.merg_sort(arr, start, mid)
            Sort.merg_sort(arr, mid + 1, end)
            Sort.merg(arr, start, mid, end)

    # helper function
    def _part(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    @staticmethod
    def quick_sort(arr, low, high):
        if low < high:
            p = Sort._part(arr, low, high)
            Sort.quick_sort(arr, low, p - 1)
            Sort.quick_sort(arr, p + 1, high)

    @staticmethod
    def heap_sort():
        pass
