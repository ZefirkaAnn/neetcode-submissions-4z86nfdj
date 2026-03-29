class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(strs[i]))+'>'+strs[i] for i in range(len(strs))])
    def decode(self, s: str) -> List[str]:
        out=[]
        while (s!=''):
            t=s.split('>', maxsplit=1)
            out.append(t[1][0:int(t[0])])
            s=t[1][int(t[0]):]
        return out