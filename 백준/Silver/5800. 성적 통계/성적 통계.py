n = int(input())

for i in range(n):
    l = list(map(int, input().split()))
    temp = []
    del l[0]
    l.sort()
    print(f'Class {i + 1}')
    
    for j in range(1, len(l)):
        temp.append(l[j] - l[j - 1])
    print(f'Max {l[len(l) - 1]}, Min {l[0]}, Largest gap {max(temp)}')