def max_hamster(S, C, hamsters):
    def swap(i, j):
        hamsters[i], hamsters[j] = hamsters[j], hamsters[i]

    def partition(left, right):
        pivot = hamsters[right][1]
        while True:
            while left <= right and hamsters[left][1] < pivot:
                left += 1
            while left <= right and hamsters[right][1] >= pivot:
                right -= 1
            if left <= right:
                swap(left, right)
                left += 1
            else:
                return right

    def quick_sort(left, right):
        if left < right:
            pivot_index = partition(left, right)
            quick_sort(left, pivot_index)
            quick_sort(pivot_index + 1, right)

    quick_sort(0, C - 1)

    total_food = 0
    count = 0
    for i in range(C):
        H, G = hamsters[i]
        additional_food = H + G * count
        if total_food + additional_food <= S:
            total_food += additional_food
            count += 1
        else:
            break
    return count


