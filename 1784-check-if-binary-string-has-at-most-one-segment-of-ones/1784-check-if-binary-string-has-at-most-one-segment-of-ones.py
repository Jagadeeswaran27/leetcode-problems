class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        for i in range(2,n):
            if s[i]=="1" and s[i-1]=="0":
                return False
        return True