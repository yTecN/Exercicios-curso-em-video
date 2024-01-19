s = 0
c = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        c += 1
        s += x
print(c)
print(s)