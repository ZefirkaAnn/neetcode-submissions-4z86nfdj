class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        dn=[nums[i+1] - nums[i] for i in range(len(nums)-1) if nums[i+1]!=nums[i]]
        e=[int(dn[i]<=1) for i in range(len(dn))]
        s=[i for i in range(len(e)) if e[i]==0 and i!=(len(e)-1)]
        t=[]
        if s!=[]:
            s=[-1]+s+[len(e)]
            for i in range(len(s)-1):
                t.append(sum(e[(s[i]+1):s[i+1]])+1)
        elif nums!=[]:
            t.append(sum(e)+1)
        else:
            t.append(0)
        return max(t)