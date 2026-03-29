class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            d["".join(sorted(i))]=[]

        for i in strs:
            d["".join(sorted(i))].append(i)

        return list(d.values())
