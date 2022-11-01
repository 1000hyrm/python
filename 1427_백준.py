l = list(map(int, input()))
l.sort(reverse=True)
print("".join(map(str, l)))