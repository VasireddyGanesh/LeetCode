class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        def temp(nums , n ,sub):
            if n==0:
                res.append(sub.copy())
                return
            sub.append(nums[n-1])
            temp(nums,n-1,sub)
            sub.remove(nums[n-1])
            temp(nums,n-1,sub)
        temp(nums,len(nums),sub)
        return res
        