class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for c in strs:
            l = [0] * 26 
            for d in c:
                l[ord(d)-ord('a')]+=1
            res[tuple(l)].append(c)
        return list(res.values() )
