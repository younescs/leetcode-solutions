class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 2:
            if target == nums[0]:
                return 0
            else: return -1
            
        l, r = 0, len(nums) -1
        output = -1

        while l < r:
            m = (l+r)//2

            if target == nums[m]:
                    return m
            if target == nums[r]:
                    return r
            if  target == nums[l]:
                    return l
            
            if nums[m] > nums[r]:
                if target > nums[m] or target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m -1
                else:
                    l = m + 1           
            
        return output

        