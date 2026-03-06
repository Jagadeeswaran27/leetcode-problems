class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n

        # left
        for i in range(n):
            if i==0:
                left[0] = height[0]
            else:
                left[i] = max(left[i-1],height[i])
        
        # right
        for i in range(n-1,-1,-1):
            if i==n-1:
                right[i] = height[i]
            else:
                right[i] = max(right[i+1],height[i])
        
        sum = 0
        for i in range(n):
            min_val = min(right[i],left[i])
            sum+=(min_val-height[i])
        
        return sum