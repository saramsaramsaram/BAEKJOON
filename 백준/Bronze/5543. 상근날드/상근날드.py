l = []
_l =[]
for i in range(3):
    n = int(input())
    l.append(n)
for i in range(2):
    n = int(input())
    _l.append(n)
print(min(l) + min(_l) - 50)