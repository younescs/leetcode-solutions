from collections import defaultdict
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        heap = []

        for i, point in enumerate(points):
            distance = (point[0]**2 + (point[1])**2)
            heapq.heappush(heap, [distance, point])

        answer = []
        for _ in range(k):
            key, value = heapq.heappop(heap)
            answer.append(value)
        
        return answer
        
        




        