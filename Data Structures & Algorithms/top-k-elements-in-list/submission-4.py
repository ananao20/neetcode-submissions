class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dictionary (element: count)
        d = defaultdict(int)
        for i in nums:
            d[i] += 1 #increase count for each element 
        sort_items = sorted(d.items(), key=lambda item: item[1], reverse=True) #sorts by values
        #d.items() returns the key value pairs
        #lambda: anonymous func telling sorted() how to sort items
        #item[0] is key & item[1] is value
        # so key=lambda item: item[1] sorts based on the values
        sort_keys = [a for a, b in sort_items] #just taking key (a) and not value (b)
        return sort_keys[:k]
#time: O(nlogn) - due to sorting
#space: O(n)