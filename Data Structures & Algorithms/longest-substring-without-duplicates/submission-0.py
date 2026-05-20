class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        i = 0
        j = 1
        window = []
        
        window.append(s[i])

        length = 1

        print(s[j])
        while j < len(s):
            if s[j] in window:
                while s[i] != s[j]:
                    i += 1
                    window.pop(0)
                i += 1
                window.pop(0)
            
            window.append(s[j])
            j += 1

            length = max(length, len(window))
        
        return length




            

        
        