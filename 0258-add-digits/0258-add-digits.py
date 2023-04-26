class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        while(num>9):    
            num=num//10+num%10
        return(num)
        