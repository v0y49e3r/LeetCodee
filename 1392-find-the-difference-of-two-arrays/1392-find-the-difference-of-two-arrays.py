class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        num1 = []
        num2 = []
        for num in set1:
            if num not in set2:
                num1.append(num)
        for num in set2:
            if num not in set1:
                num2.append(num)
        return [num1, num2]
