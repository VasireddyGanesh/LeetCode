class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        sum=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                    l=[i,j]
                    break
        return l
                    
        