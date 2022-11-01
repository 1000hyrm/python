num = int(input())
l = []
for i in range(num) :
    x, y = map(int, input().split(' ')) #1 -1
    l.append((x, y))

l = sorted(l, key=lambda x : (x[0],x[1]))
#첫 번째 인자를 기준으로 오름차순, 그 안에서 두번째 인자를 기준으로 오름차순 정렬
#두번째 인자를 내림차순으로 하고 싶으면 x : (x[0], -x[1])
for i in l :
    print(i[0], i[1])