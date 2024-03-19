def binary_search_hamster(arr, item, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid][1] < item[1]:
            start = mid + 1
        elif arr[mid][1] > item[1]:
            end = mid - 1
        else:
            return mid
    return start 

def hamster_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        pos = binary_search_hamster(arr, temp, 0, i - 1)
        arr = arr[:pos] + [temp] + arr[pos:i] + arr[i+1:]
    return arr

def max_hamsters_with_sort(S, C, hamsters):
    sorted_hamsters = hamster_sort(hamsters)
    
    max_hamsters = 0
    total_food = 0

    for i in range(C):
        additional_food = sorted_hamsters[i][1] * max_hamsters
        if total_food + sorted_hamsters[i][0] + additional_food <= S:
            total_food += sorted_hamsters[i][0] + additional_food
            max_hamsters += 1
        else:
            break

    return max_hamsters


example1_binary = max_hamsters_with_sort(7, 3, [[1, 2], [2, 2], [3, 1]])  
example2_binary = max_hamsters_with_sort(19, 4, [[5, 0], [2, 2], [1, 4], [5, 1]])  
example3_binary = max_hamsters_with_sort(2, 2, [[1, 50000], [1, 60000]])  

print(f'Приклад 1: {example1_binary}\nПриклад 2: {example2_binary}\nПриклад 3: {example3_binary}')


