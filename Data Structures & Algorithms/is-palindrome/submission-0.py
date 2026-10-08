class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = ""
        for c in s:
            if ord(c)>=ord('A') and ord(c)<=ord('Z'):
                v+=c
            elif ord(c)>=ord('a') and ord(c)<=ord('z'):
                v+=c
            elif ord(c)>=ord('0') and ord(c)<=ord('9'):
                v+=c
            else:
                pass
        v=v.lower()
        print(v)
        t = v[::-1]
        if v==t:
            return True
        else:
            return False