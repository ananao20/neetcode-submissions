class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for c in nums:
            d[c] = d.get(c,0)+1
        f = dict(sorted(d.items(),key=lambda item: item[1],reverse=True))
        g = list(f.keys())[:k]
       
        return list(g)