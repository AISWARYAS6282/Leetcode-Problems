class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
        # Update current element to be sum of itself and previous running sum
            nums[i] += nums[i - 1]
        return nums