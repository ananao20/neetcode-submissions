class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): 
            return False
        d = defaultdict(int)
        for c,g in zip(s,t):
            d[c] += 1
            d[g] -= 1
        for c in d:
            if d[c] != 0:
                return False
        return True
