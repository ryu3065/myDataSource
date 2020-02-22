def twoSum(nums, target):
  if len(nums) < 2:
    return False

  for i in range(1, len(nums)):
    if target - (nums[0] + nums[i]) == 0:
      result = [nums.index(0),nums.index(i)]
      return print(result)
  return print(twoSum(nums[i:],target))

    


nums = [2, 7, 11, 15]
target = 9

twoSum(nums, target)