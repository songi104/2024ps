# 재귀함수 이용한 binary Search

def binary_search(arr, target, start, end):
    mid = (start+end)//2
    print(start, end, f'mid val: {arr[mid]}')
    if start > end:
        print(start, end)
        return None
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)


n, target = [10, 7]
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(arr, target, 0, n))
