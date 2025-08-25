class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(height) -1
        maxAmount = 0
        while l < r:
            amount = min(height[l], height[r]) * (r - l)
            maxAmount = max(amount, maxAmount)
            if height[r] > height[l]:
                l += 1
            elif height[r] < height[l]:
                r -=1
            else:
                l +=1
                r-=1
        return maxAmount
            