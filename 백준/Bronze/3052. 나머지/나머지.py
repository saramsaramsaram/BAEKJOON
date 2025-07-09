l = []

for i in range(10):
    a = int(input())
    if not a % 42 in l:
        l.append(a % 42)
print(len(l))