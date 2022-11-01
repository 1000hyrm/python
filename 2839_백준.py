n = input()
n = int(n)
cnt = 0

while n >= 0 : 
  if n % 5 == 0 :
    cnt = cnt + (n // 5) #몫이 들고갈거
    print(cnt)
    break
  n = n - 3
  cnt = cnt + 1
  
else :
  print(-1)