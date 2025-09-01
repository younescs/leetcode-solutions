class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for e in s:
            if e == "{":
                stack.append("}")
            elif e == "(":
                stack.append(")")
            elif e == "[":
                stack.append("]")
            else:
                if not stack or e != stack[-1]:
                    return False
                stack.pop()
                
        return not stack
                



        
        