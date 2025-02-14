class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        a, b = len(str1), len(str2)
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return str1[:a]


