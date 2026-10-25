import math
from collections import defaultdict
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        #[[1,3],[-2,2]]
        #dist_to_points : [/10: [1,3], /8: [-2,2]]
        # heap: /10
        # answer : [[-2,2]]

        heap = []
        distance_to_points = defaultdict(list)

        for i, point in enumerate(points):
            distance = math.sqrt((point[0])**2 + (point[1])**2)

            heapq.heappush(heap, distance)
            distance_to_points[distance].append(point)

        answer = []
        for _ in range(k):
            key = heapq.heappop(heap)
            for i in range(len(distance_to_points[key])):
                answer.append(distance_to_points[key][i])
                if len(answer) == k:
                    return answer
        
        return answer
        
        




        