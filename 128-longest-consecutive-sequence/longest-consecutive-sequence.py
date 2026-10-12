class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums: return 0
        numset = set(nums)
        counter = 1
        for num in numset:
            if (num + 1) not in numset or (num - 1) in numset:
                continue
            else:
                new_counter = 0
                i = 0
                while (num + i) in numset:
                    new_counter += 1
                    i += 1
                counter = max(counter, new_counter)

        return counter
