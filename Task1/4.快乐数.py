"""
因为会有无限循环，所以仅需判断n是否存在hash表中即可
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        hash_map = {}
        while n not in hash_map:
            hash_map[n] = 0
            n = sum([int(num) ** 2 for num in str(n)])
            if n == 1:
                return True
        return False
