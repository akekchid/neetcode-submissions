class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        numSet = set()

        for i in nums:
            numSet.add(i)

        count = 0
        maxCount = 0
        
        for i in range(min(nums), max(nums) + 1):
            if i in numSet:
                count += 1

            else:
                count = 0

            maxCount = max(maxCount, count)

        return maxCount

             

        