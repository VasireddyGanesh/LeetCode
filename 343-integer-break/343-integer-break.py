class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        
        multiple  = n // 3
        remainder = n % 3
        
        
        #Take 10 for example, we can break it down to 
        #3 x 3 x 3 x 1 < 3 x 3 x 4
        if remainder == 1:
            multiple  -= 1
            return 3 ** multiple * 4
        
        if remainder == 2:
            return 3 ** multiple  * remainder
		# The else case is remainder == 0
        return 3 ** multiple 
        