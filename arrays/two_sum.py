# LeetCode 1: Two Sum
# Time: O(n)
# Space: O(n)

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 16], 9))
