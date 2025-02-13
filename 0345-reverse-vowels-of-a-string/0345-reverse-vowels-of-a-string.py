class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        stack = []
        result = []
        for c in s:
            if c in vowels:
                stack.append(c)
        for c in s:
            if c in vowels:
                result.append(stack.pop())
            else:
                result.append(c)

        return "".join(result)
