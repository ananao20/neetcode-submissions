class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for c in nums:
            d[c] += 1
        f = dict(sorted(d.items(),key=lambda item: item[1],reverse=True))
        g = list(f.keys())[:k]
       
        return g