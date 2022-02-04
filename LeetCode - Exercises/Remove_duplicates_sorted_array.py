def unique_number(arr):
    for i in range(len(arr)-1,0,-1):
        if arr[i-1]==arr[i]:
            del arr[i]
    return arr