l = list(map(int, input().split()))
res = []
sor = []

for i in l :
    res.append(i)
    sor.append(i)
#print("입력", res)
#print("입력2", sor)

sor.sort()
#print("정렬", sor)

while True :
    for i in range(len(res) - 1) :
        if res[i] > res[i+1] :
            temp = res[i]
            res[i] = res[i+1]
            res[i+1] = temp
            print(" ".join(map(str, res))) #황당 그 자체 ,랑 []가 있는게 죄냐
    if sor == res :
        #print("완")
        break