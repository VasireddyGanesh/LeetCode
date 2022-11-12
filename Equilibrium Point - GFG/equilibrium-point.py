# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        if len(A)==1:
            return 1
        s=sum(A)
        temp=s-A[0]
        for i in range(1,len(A)):
            temp -= A[i] 
            if i<len(A)-1 and temp*2 == s-A[i]:
                return i+1
        return -1



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends