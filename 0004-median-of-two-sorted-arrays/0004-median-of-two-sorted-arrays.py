class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=j=0
        new_nums = []

        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                new_nums.append(nums1[i])
                i+=1
            else:
                new_nums.append(nums2[j])
                j+=1
        
        while i<len(nums1):
            new_nums.append(nums1[i])
            i+=1
        
        while j<len(nums2):
            new_nums.append(nums2[j])
            j+=1
        
        n = len(new_nums)

        if n%2 == 0:
            return (new_nums[(n//2)-1]+new_nums[n//2])/2
        else:
            return new_nums[n//2]