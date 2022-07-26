class Solution:
    def minOperations(self, nums: List[int]) -> int:
        max=nums[0]
        count=0
        for i in range(1,len(nums)):
            if max>=nums[i]:
                count+=((max+1)-nums[i])
                nums[i]=max+1
            max=nums[i]
        return count
        