class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        len_s = len(s)
        l, r = 0, len_s - 1
        while l < r:
            while l < len_s and not s[l].isalnum():
                l += 1
            while r > -1 and not s[r].isalnum():
                r -= 1
            
            if l < len_s and r > -1 and s[l] != s[r]:
                return False
            l += 1
            r -= 1
            
        return True
        