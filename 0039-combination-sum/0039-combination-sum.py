class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        n = len(candidates)
        self.calc(n,0,candidates,res,target,temp)
        return res

    def calc(self,n,idx,nums,res,diff,temp):
            if diff == 0:
                res.append(temp[::])
                return
            for i in range(idx,n):
                if diff < nums[i]:
                    continue
                temp.append(nums[i])
                self.calc(n,i,nums,res,diff-nums[i],temp)
                temp.remove(nums[i])