class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.find(0,0,n,res,'')
        return res
    
    def find(self,closed,opened,n,res,s):
        if closed==n:
            res.append(s)
            return
        
        if opened<n:
            self.find(closed,opened+1,n,res,s+'(')
        
        if closed<opened:
            self.find(closed+1,opened,n,res,s+')')