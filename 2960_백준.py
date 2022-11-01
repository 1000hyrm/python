n, k = map(int, input().split()) #n과 k 입력받기
res = [] #2부터 n까지 나열할 리스트 선언
cnt = 0
num = 0 #결과값

for i in range(2, n+1) :
    res.append(i) #리스트에 2부터 n까지 삽입

while True :
    a = min(res) #리스트의 가장 작은 원소
    res.remove(a)

    cnt += 1 
    
    if cnt == k : #cnt가 k와 같을 경우
        num = a #지운 가장 작은 원소를 num으로 삽입
        print(num)

    for i in res : 
        if i % a == 0 : #지우지 않은 수의 배수
            res.remove(i)
            cnt += 1
            if cnt == k :
                num = i
                print(num)

    if len(res) == 0 : #모든 수를 지운 경우
        break