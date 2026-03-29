class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d.keys():
                d[i]=0
            else:
                d[i]+=1
        sorted_d = sorted(d.items(), key=lambda kv: kv[1])
        return [sorted_d[-k:][i][0] for i in range(k)]