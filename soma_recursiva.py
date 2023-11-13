def soma(arr):
    if arr == []:
        return 0
    else:
        first = arr[0]
        arr = arr[1:]
        return first + soma(arr)

print(soma([2,4,6,1]))

