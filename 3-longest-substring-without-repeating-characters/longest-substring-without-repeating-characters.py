class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l,r = 0, 0
        counter, new_counter = 0, 0

        while l <= r and r < len(s):
            while s[r] in seen:
                    seen.remove(s[l])
                    new_counter -= 1
                    l += 1
            if s[r] not in seen:
                seen.add(s[r])
                new_counter += 1
            r += 1
            counter = max(counter, new_counter)

        return counter