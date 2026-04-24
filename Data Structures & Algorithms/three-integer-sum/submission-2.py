class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        nums.sort()

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                triplet = [nums[i], nums[l], nums[r]]
                total = nums[i] + nums[l] + nums[r]
                
                if total > 0:
                    r -= 1
                if total < 0:
                    l += 1

                if total == 0:
                    if triplet not in res:
                        res.append(triplet)
                    r -= 1

        
        return res
                    
