def conta_items(arr: list):
    if arr == []:
        return 0
    else:
        return 1 + conta_items(arr[1:])

print(conta_items([1,2,3,4,5,6,7]))