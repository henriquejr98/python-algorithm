def maior(arr: list):
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[0] < arr[1]:
            arr.pop(0)
            return maior(arr)
        else:
            arr.pop(1)
            return maior(arr)

print(maior([1,89,28,34,162,7,1584,5,8]))
