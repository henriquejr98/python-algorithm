def binary_search(array, num):
    low = 0
    high = len(array) - 1
    counter = 0

    while low <= high:
        counter += 1
        mid = (low + high) // 2
        if array[mid] == num:
            return mid, counter
        elif array[mid] > num:
            high = mid - 1
        elif array[mid] < num:
            low = mid + 1
        else:
            return None




my_list = [1, 3, 5, 7, 12, 15, 18, 23]
#              0    1   2   3   4
my_sec_list = [10, 20, 30, 40, 50]
wanted = 15
print(binary_search(my_list, wanted)) # 5
print(binary_search(my_sec_list, 50))