class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums2 = []
        for ele in nums:
            if ele not in nums2:
                nums2.append(ele)
        return nums2
    
        
        
sol = Solution()
print(sol.removeDuplicates([1,1,2]))