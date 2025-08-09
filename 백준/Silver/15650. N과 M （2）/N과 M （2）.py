from itertools import combinations


a,b= map(int,input().split())
for i in combinations([_ for _ in range(1,a+1)], b):
    for j in i:
        print(j, end=" ")
    print()