"""
首先将所有的数字出现的次数存入hash_map,同时，也存入neg和pos
将所有的数字分为负数和正数，neg + pos + x = 0
两层循环，遍历neg，然后遍历pos，x = -(neg+pos)，
如果x在hash_map中出现，会出现两种情况：
1. x == neg or pos， 那么需要判断hash_map[x] >= 2
2. neg < x < pos
"""
class Solution:
    def threeSum(self, nums):
        if not nums:
            return None
        pos = {}
        neg = {}
        hash_map = {}
        result = []
        for num in nums:
            if num > 0:
                pos[num] = pos.setdefault(num, 0) + 1
            elif num < 0:
                neg[num] = neg.setdefault(num, 0) + 1
            hash_map[num] = hash_map.setdefault(num, 0) + 1
        if 0 in hash_map and hash_map[0] > 2:
            result.append([0, 0, 0])

        for n in neg:
            for p in pos:
                target = -n - p
                if target in hash_map:
                    if target in [p, n] and hash_map[target] > 1:
                        result.append([p, n, target])
                    elif n < target < p:
                        result.append([n, target, p])

        return result
