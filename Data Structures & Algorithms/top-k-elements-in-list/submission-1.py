class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dictionary (element: count)
        d = defaultdict(int)
        c=0
        for i in nums:
            d[i] += 1
        sort_val = sorted(d.items(), key=lambda item: item[1], reverse=True)
        # sort_val = sorted(d.items(), reverse=True)
        sort_keys = [k for k, v in sort_val]
        return sort_keys[:k]