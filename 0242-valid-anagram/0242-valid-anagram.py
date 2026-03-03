class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_dict = {}
        s_dict = {}

        for i in range(len(s)):
            t_dict[t[i]] = 1+t_dict.get(t[i],0)
            s_dict[s[i]] = 1+s_dict.get(s[i],0)
        
        return t_dict==s_dict