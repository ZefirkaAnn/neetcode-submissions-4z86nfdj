class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(' ', '').lower()
        for l in s.replace(' ', '').lower():
            if not ((ord(l)>=ord('a') and ord(l)<=ord('z')) or (ord(l)>=ord('0') and ord(l)<=ord('9'))):
                s=s.replace(l, '')

        if len(s)%2==0:
            return (s[:len(s)//2]==s[len(s)//2:][::-1])
        else:
            return (s[:len(s)//2]==s[len(s)//2+1:][::-1])