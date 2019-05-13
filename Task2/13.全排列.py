class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for x in nums:
            ys=nums[:]
            ys.remove(x)
            for y in self.permute(ys):
                res.append([x]+y)
        return res