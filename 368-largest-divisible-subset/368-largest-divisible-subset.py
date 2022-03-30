class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        divSet=[ [num] for num in nums ]
        
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i]%nums[j]==0) and len(divSet[i]) < len(divSet[j])+1:
                    divSet[i]=divSet[j]+[nums[i]]
        return max(divSet,key=len)
        