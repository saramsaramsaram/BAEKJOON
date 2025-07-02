nums = list(map(int, input().split()))
nums.sort()

for i in range(4):
    for j in range(-200, 201):
        temp = nums[:]
        temp.insert(i, j)
        temp.sort()
        d = temp[1] - temp[0]
        if all(temp[k+1] - temp[k] == d for k in range(3)):
            if j not in nums:
                print(j)
                exit()
