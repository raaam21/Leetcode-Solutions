class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        def f(idx):
            if idx>=len(nums)-1:
                return 0

            
            if dp[idx]!=-1:
                return dp[idx]


            temp=float('-inf')
            for i in range(idx+1,len(nums)):
                v=nums[i]-nums[idx]
                if -target<=v<=target:  
                    temp=max(temp,f(i)+1)

            dp[idx]=temp
            return temp

        dp=[-1 for i in range(len(nums))]
        ans=f(0)
        if ans>0:
            return ans
        return -1

