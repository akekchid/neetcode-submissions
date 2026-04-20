class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        # char and occurrences
        words1 = {}
        words2 = {}


        for i in range(len(s)):
            words1[s[i]] = words1.get(s[i], 0) + 1
            words2[t[i]] = words2.get(t[i], 0) + 1

        if words1 == words2:
            return True

        return False

        
        


