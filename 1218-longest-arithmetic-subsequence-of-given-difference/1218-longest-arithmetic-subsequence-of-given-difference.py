class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp=[-1 for i in range(len(arr))]
        imap=defaultdict(list)
        for i in range(len(arr)):
            imap[arr[i]].append(i)
        # print(imap)

        for i in range(len(arr)):
            if dp[i]==-1:
                t=1
                v=arr[i]-difference
                if v in imap.keys():
                    for idx in imap[v]:
                        if idx<i:
                            t=max(t,dp[idx]+1)
                dp[i]=t
        
        # print(dp)
        return max(dp)

