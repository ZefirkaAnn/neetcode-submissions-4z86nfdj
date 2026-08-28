class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        k = 0

        while i != j:
            if min(height[i], height[j]) * (j-i) > k:
                k = min(height[i], height[j]) * (j-i)
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
        return k