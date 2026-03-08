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
    def merge_sort():
        pass

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

    @staticmethod
    def shell_sort():
        pass

    @staticmethod
    def tree_sort():
        pass

    @staticmethod
    def cycle_sort():
        pass

    @staticmethod
    def comb_sort():
        pass

    @staticmethod
    def cocktail_shaker_sort():
        pass

    @staticmethod
    def gnome_sort():
        pass

    @staticmethod
    def odd_Even_sort():
        pass

    @staticmethod
    def pancake_sort():
        pass

    @staticmethod
    def strand_sort():
        pass

    @staticmethod
    def bitonic_sort():
        pass

    @staticmethod
    def smooth_sort():
        pass

    @staticmethod
    def intro_sort():
        pass

    @staticmethod
    def tim_sort():
        pass


# Batcher’s Odd–Even Mergesort
