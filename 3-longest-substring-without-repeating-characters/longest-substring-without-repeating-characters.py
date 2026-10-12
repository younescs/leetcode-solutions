class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        counter = 0

        for r, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(ch)
            counter = max(counter, r - l + 1)

        return counter