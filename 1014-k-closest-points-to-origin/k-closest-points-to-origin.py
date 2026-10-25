class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        heap = []

        for point in points:
            distance = (point[0]**2 + (point[1])**2)
            heap.append((distance, point))

        heapq.heapify(heap)
        answer = []
        for _ in range(k):
            key, value = heapq.heappop(heap)
            answer.append(value)
        
        return answer
        
        




        