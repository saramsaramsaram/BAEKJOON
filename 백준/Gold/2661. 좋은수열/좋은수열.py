def is_good(s):
    length = len(s)
    for i in range(1, length // 2 + 1):
        if s[-i:] == s[-2*i:-i]:
            return False
    return True

def dfs(s, n):
    if len(s) == n:
        print(s)
        exit(0)

    for digit in '123':
        new_s = s + digit
        if is_good(new_s):
            dfs(new_s, n)

N = int(input())
dfs('', N)


