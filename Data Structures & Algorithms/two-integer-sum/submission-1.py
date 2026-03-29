class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind=[]
        for i in range(len(nums)):
            if (target - nums[i]) in nums[:i]+nums[i+1:]:
                ind.append(i)
        return ind
