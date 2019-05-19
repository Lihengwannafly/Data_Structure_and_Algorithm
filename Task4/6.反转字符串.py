class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s:
            n = len(s)
            mid = n // 2
            start = 0
            while start < mid:
                s[start], s[n-start-1] = s[n-start-1], s[start]
                start += 1