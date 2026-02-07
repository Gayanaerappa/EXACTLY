nums = [1, 2, 2, 3, 3, 3]

for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
    print(nums[i], "appears", count, "times")