class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        out=[]
        if nums[0] >0 or nums[-1] <0:
            return out
        else:
            i=0
            while i != len(nums)-2:
                k=i+1
                j=len(nums)-1

                while k<j:
                    sum = nums[i] + nums[k] + nums[j]
                    if sum == 0:
                        out.append([nums[i], nums[k], nums[j]])
                        while k!=len(nums)-2 and nums[k] == nums[k+1]:
                            k+=1
                        k+=1
                        print(k)
                        while j != 1 and nums[j] == nums[j-1]:
                            j-=1
                        j-=1
                        print(j)
                    elif sum > 0:
                        j-=1
                    elif sum < 0:
                        k+=1
                i+=1
                while nums[i] == nums[i-1] and i!=len(nums)-2:
                    i+=1
            return out