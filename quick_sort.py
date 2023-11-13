def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        maiores = [x for x in arr[1:] if x > arr[0]]
        menores = [x for x in arr[1:] if x < arr[0]]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)

print(quick_sort([5,8,1,17]))