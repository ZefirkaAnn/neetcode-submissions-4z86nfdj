class Solution:
    def isValid(self, s: str) -> bool:
        d = []
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in ["(", "[", "{"]:
                d.append(i)
            else:
                if len(d) == 0:
                     return False
                elif (ord(i) - ord(d[-1]) != 1) and (ord(i) - ord(d[-1]) != 2):
                    return False
                else:
                    d.pop()
        return len(d) == 0