#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # count0=0
        # count1=0
        # count2=0
        # for i in arr:
        #     if i==0:
        #         count0 +=1
        #     elif i==1:
        #         count1 +=1
        #     else:
        #         count2 +=1
        return arr.sort()



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends