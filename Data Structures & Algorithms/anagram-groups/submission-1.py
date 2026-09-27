class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) #here don't use d = {}
        for i in strs:
            s = "".join(sorted(i)) # sorts each string alphabetically, making anagrams identical
            d[s].append(i) # appends the original word to the sorted key's list
        return list(d.values())