nums = [2, 6, 7, 14, 5, 9]

for i in range(len(nums)):
    nums[i] = nums[i] * nums[i]
    # nums[i] *= nums[i]
    # nums[i] **= 2

print(nums)  # [4, 36, 49, 196, 25, 81], in place
