class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        st=[1]*(len(nums))
        st[1]=nums[0]

        end=[1]*(len(nums))
        end[1]=nums[-1]

        for i in range(1, len(nums)-1):
            st[i+1]=st[i]*nums[i]
            end[i+1]=end[i]*nums[-i-1]

        return  [i*j for i, j in zip(st, end[::-1])]