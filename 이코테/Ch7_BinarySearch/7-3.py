def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1


n, target = [10, 7]
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(arr, target, 0, n))
