class Solution(object):
    def threeSum(self, nums):
        finalAnswers = set()
        
        for a in range(len(nums)):
            anchor = nums[a]
            dico2sum = {}
            
            for i in range(a+1, len(nums)):
                target = - (anchor + nums[i])
                
                if target in dico2sum:
                    triplet = tuple(sorted([anchor, nums[i], target]))
                    finalAnswers.add(triplet)
                else:
                    dico2sum[nums[i]] = i
        
        return list(finalAnswers)
