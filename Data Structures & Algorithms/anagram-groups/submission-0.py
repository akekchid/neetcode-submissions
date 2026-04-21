class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            sortedS = ''.join(sorted(i))
            hashmap[sortedS].append(i)

        return list(hashmap.values())

        

        
