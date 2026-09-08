class Solution:
    def trap(self, h: List[int]) -> int:
        i=0
        i_=0
        j=len(h) -1
        j_ = len(h) -1
        s = 0

        while i_ < j_:
            if h[i] == 0:
                i+=1
                i_=i
            elif h[j] == 0:
                j-=1
                j_=j
            else:
                if h[i] <= h[j]:
                    i_+=1
                    if h[i_] >= h[i]:
                        s+=h[i] * (i_-i -1)
                        i=i_
                    else:
                        s-=h[i_]
                else:
                    j_-= 1
                    if h[j_] >= h[j]:
                        s+=h[j] * (j-j_-1)
                        j=j_
                    else:
                        s-=h[j_]
        return s