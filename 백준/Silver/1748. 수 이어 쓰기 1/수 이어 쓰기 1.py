n = int(input())
length = 0
digit = 1
start = 1

while start * 10 <= n:
    end = start * 10 - 1
    count = end - start + 1
    length += count * digit
    start *= 10
    digit += 1

length += (n - start + 1) * digit

print(length)
