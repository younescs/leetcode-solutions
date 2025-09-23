from collections import deque
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
     
        first = deque(word1)
        second = deque(word2)
        word3 = []
        length = len(word1)+len(word2)
        while length:
            if first:
                letter = first.popleft()
                word3.append(letter)
            if second:
                letter = second.popleft()
                word3.append(letter)
            length -=1

        word3 = "".join(word3)
        return word3