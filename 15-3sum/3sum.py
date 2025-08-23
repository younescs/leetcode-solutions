class Solution(object):
    def threeSum(self, nums):
    
        nums.sort()
        res = []
        anchor = 0
        while anchor < len(nums) - 2:

            if anchor > 0 and nums[anchor] == nums[anchor-1]:
                anchor += 1
                continue

            l = anchor +1
            r = len(nums)-1

            while l < r:
                if nums[anchor] + nums[l] + nums[r] == 0:
                    res.append([nums[anchor],nums[l],nums[r]])
                    l += 1
                    r -=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1

                elif nums[anchor] + nums[l] + nums[r] < 0:
                    l += 1
                    

                elif nums[anchor] + nums[l] + nums[r] > 0:
                    r -= 1

            anchor +=1

        return res

            