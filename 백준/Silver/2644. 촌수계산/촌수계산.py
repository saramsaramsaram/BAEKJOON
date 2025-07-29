from collections import deque

n = int(input())
start_person, end_person = map(int, input().split())
relations_count = int(input())

family = [[] for _ in range(n+1)]

for _ in range(relations_count):
    parent, child = map(int, input().split())
    family[parent].append(child)
    family[child].append(parent)

def bfs(start, end):
    visited = [False] * (n+1)
    distance = [-1] * (n+1)
    queue = deque([start])
    visited[start] = True
    distance[start] = 0

    while queue:
        current = queue.popleft()
        if current == end:
            return distance[current]
        for relative in family[current]:
            if not visited[relative]:
                visited[relative] = True
                distance[relative] = distance[current] + 1
                queue.append(relative)
    return -1

print(bfs(start_person, end_person))