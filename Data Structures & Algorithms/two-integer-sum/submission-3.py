class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i,n in enumerate(nums):
            if (n in h) and (h[n] != i) :
                return [h[n],i]
            else:
                 h[target-n] = i
        return []