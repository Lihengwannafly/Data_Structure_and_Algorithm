"""
从后往前开始合并会比较方便
"""
class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = m + n - 1
        m = m - 1
        n = n - 1
        while n >= 0 and m >= 0:
            if nums1[m] >= nums2[n]:
                nums1[pos] = nums1[m]
                m = m - 1
            else:
                nums1[pos] = nums2[n]
                n = n - 1
            pos = pos - 1

        while n >= 0:
            nums1[pos] = nums2[n]
            pos -= 1
            n -= 1
