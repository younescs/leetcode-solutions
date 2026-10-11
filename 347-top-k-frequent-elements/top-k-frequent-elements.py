from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        counts = defaultdict(int)
        counts = Counter(nums)
        

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in counts.items():
            buckets[value].append(key)

        result = []
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result



        

       
            

        
        