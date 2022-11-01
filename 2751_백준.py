#못 풂
import sys

num = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for i in range(num)]
'''
def quick_sort(arr, start, end) :
    if start >= end :
        return
    pivot = start
    left = start + 1
    right = end

    while(left <= right) :
        while(left <= end and arr[left] <= arr[pivot]):
            left += 1
        while(right > start and arr[right] >= arr[pivot]) :
            right -= 1
        if(left > right) :
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else :
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right+1, end)

quick_sort(arr, 0, len(arr)-1)

for i in range(len(arr)) :
    min_idx = i
    for j in range(i+1, len(arr)) :
        if arr[min_idx] > arr[j] :
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
'''

print(*arr, sep='\n')