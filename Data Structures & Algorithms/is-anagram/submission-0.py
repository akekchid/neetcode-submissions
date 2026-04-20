class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        # char and occurrences
        words1 = {}
        words2 = {}


        for i in range(len(s)):
            if s[i] not in words1:
                words1[s[i]] = 1
            else:
                words1[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in words2:
                words2[t[i]] = 1
            else:
                words2[t[i]] += 1

        if words1 == words2:
            return True

        return False

        
        


