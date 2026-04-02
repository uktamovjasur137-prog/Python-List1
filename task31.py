nums = [1, 2, 3, 6, 8, 1, 1, 4, 3, 1, 2, 1]

max_num = [0]

for num in nums:
    if nums.count(num) > nums.count(max_num):
        max_num = num

print(max_num)