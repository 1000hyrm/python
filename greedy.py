n = int(input()) #낸 돈
cnt = 0
money = [500, 100, 50, 10, 5, 1]
n = 1000 - n

for i in money :
    cnt += (int)(n / i) #//를 써도 되지만, 보고 해서 걍..양심.,.,
    n = n % i
    
print(cnt)