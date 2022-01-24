def climbing_stairs(n):
    steps_stair = [1,1]
    for i in range(2,n+1):
        steps_stair.append(steps_stair[i-1]+steps_stair[i-2])
    return steps_stair[n]