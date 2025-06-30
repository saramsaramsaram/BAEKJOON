a = input()
l = [0 for i in range(26)]
for i in a:
    l[ord(i) - ord('a')] += 1

for i in l:
    print(i, end=' ')