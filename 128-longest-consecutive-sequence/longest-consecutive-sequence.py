class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
 
        numset = set(nums)
        counter = 0
        for num in numset:
            if (num - 1) in numset:
                continue
            else:
                i = 0
                while (num + i) in numset:
                    i += 1
                counter = max(counter, i)

        return counter
