class solution:
    def containsDuplicate(self,nums):
        seen = set()  #to store seen numbers 
        for num in nums: #iterate through each number
            if num in seen: #if number is already in seen set,
                return True #duplicate found - function ends here
            seen.add(num) # runs ONLY if no duplicate found # add number to seen set
        return False # no duplicates found after checking all numbers
    
if __name__ == "__main__":
    sol = solution()
    nums = [1,2,3,4,4,5,5]
    result = sol.containsDuplicate(nums)
    print(f"Contains duplicates: {result}")  # Output: True