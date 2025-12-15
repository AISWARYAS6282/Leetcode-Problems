class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1  # index where the next unique element goes

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = sol.removeDuplicates(nums)
    print (f"k={k} \nSorted array updated={nums[:k]}")
  # Output: 5
