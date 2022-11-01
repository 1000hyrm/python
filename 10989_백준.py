#못 풂
import sys

num = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for i in range(num)]
print(arr)

arr.sort()

print(*arr, sep='\n')