class Solution(object):
    def twoSum(self, nums, target):
       for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


sol = Solution()
nums = [2, 7, 11, 15]
target = 9
ouput = sol.twoSum(nums, target)
print(ouput)
