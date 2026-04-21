class Solution(object):
    def subsets(self, nums):
        res = [[]]
        
        for num in nums:
            tmp = []
            for i in range(len(res)):
                dummy = res[i] + [num]   # create NEW list
                tmp.append(dummy)
            res.extend(tmp)

        return res