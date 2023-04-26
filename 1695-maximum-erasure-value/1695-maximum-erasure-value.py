class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d={}
        ws=0
        we=0
        ans=0
        sumit=0
        while(we<len(nums)):
            while(we<len(nums) and nums[we] not in d):
                sumit+=nums[we]
                d[nums[we]]=1
                we+=1
            else:
                ans=max(ans,sumit)
                sumit-=nums[ws]
                del d[nums[ws]]
                ws+=1
        return ans


