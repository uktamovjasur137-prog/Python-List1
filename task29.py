nums = [1, 2, 3, 4, 7, 6, 7, 1, 2, 3, 9, 5]

unique_nums = []

for num in nums:
    if nums.count(num) == 1:
        unique_nums.append(num)

print(unique_nums)
           