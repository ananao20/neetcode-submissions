class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) #here don't use d = {}
        for i in strs:
            s = "".join(sorted(i))
            d[s].append(i)
        return list(d.values())