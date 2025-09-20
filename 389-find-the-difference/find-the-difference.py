class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        lst_s = [0] * 26

        for char in s:
            lst_s[ord(char) - ord('a')] +=1
        
        for char in t:
            if lst_s[ord(char) - ord('a')] > 0:
                lst_s[ord(char) - ord('a')] -= 1
            else:
                return char
            