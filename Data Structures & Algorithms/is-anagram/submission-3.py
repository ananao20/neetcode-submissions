class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): 
            return False
        d = {}
        for c,g in zip(s,t):
            d[c] = d.get(c,0)+1
            d[g] = d.get(g,0)-1
        for c in d:
            if d[c] != 0:
                return False
        return True
