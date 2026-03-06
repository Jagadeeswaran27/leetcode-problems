class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[-1]
        if n==2:
            return max(nums[0],nums[1])

        temp=[0]*n
        for i in range(n):
            if i==0:
                temp[i] = nums[i]
            elif i==1:
                temp[i] = max(nums[0],nums[1])
            else:
                temp[i] = max(temp[i-1],nums[i]+temp[i-2])
        
        return temp[-1]