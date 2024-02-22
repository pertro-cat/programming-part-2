def seeding_plan(m ,n , seeds_in_each_place):
    planting_plan = []
    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                planting_plan.append(seeds_in_each_place[i][j])
        else:
            for j in range(n-1, -1, -1):
                planting_plan.append(seeds_in_each_place[i][j])
    return planting_plan
print(seeding_plan(5, 5, [[1, 2, 3, 4, 5], 
                          [6, 7, 8, 9, 10], 
                          [11, 12, 13, 14, 15], 
                          [16, 17, 18, 19, 20], 
                          [21, 22, 23, 24, 25]]))   

 
