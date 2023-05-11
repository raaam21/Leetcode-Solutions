class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0 for i in range(len(nums2)+1)]for j in range(len(nums1)+1)]
        for i in range(len(dp)):
            dp[i][0]=1
        for j in range(len(dp[0])):
            dp[0][j]=1

        # print(dp)
       
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    dp[i+1][j+1]=1+dp[i][j]
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
        
        return dp[-1][-1]-1