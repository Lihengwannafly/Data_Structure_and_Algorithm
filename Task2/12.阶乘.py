class Solution:
    def factorial(self, N: int) -> int:
        if N == 0:
            return 1
        if N == 1:
            return 1
        else:
            return N * self.factorial(N-1)



