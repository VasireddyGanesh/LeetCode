class Solution:
    def minimumSum(self, num: int) -> int:
        num=list(str(num))
        num.sort()
        num1=int(num[0]) * 10 + int(num[2])
        num2=int(num[1]) * 10 + int(num[3])
        return num1+num2
        