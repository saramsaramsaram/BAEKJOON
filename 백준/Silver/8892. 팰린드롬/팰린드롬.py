def is_palindrome(s):
    return s == s[::-1]

T = int(input())
for _ in range(T):
    n = int(input())
    strings = [input() for _ in range(n)]
    found = False

    for i in range(n):
        for j in range(n):
            if i != j:
                combined = strings[i] + strings[j]
                if is_palindrome(combined):
                    print(combined)
                    found = True
                    break
        if found:
            break
    if not found:
        print(0)
