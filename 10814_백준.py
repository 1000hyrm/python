num = int(input())
l = []
for i in range(num) :
    age, name = map(str, input().split(' ')) #21 Junkyu
    l.append((int(age), name))

l = sorted(l, key=lambda x:x[0])

for i in l :
    print(i[0], i[1])