def max_hamster(S, C, hamster):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(hamster) - 1):
            if hamster[i][1] < hamster[i + 1][1]:
                hamster[i], hamster[i + 1] = hamster[i + 1], hamster[i]
                is_sorted = False

    total_food = 0
    count = 0
    for i in range (C):
        H, G = hamster[i]
        additional_food = H + G * count
        if total_food + additional_food <= S:
            total_food += additional_food
            count += 1
        else:    
            break
    return count

print(max_hamster(7, 3, [[1, 2], [2, 2], [3, 1]]))

