class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        res = []
        
        for i in range(len(nums)):
            freqmap[nums[i]] = freqmap.get(nums[i], 0) + 1

        for i in range(k):
            maxkey = max(freqmap, key=freqmap.get)
            res.append(maxkey)
            del freqmap[maxkey]

        return res
            
