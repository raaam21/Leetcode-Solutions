class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ws=0
        we=0
        ans=0
        cnt=0
        while(we<len(s)):
            while(we<len(s) and we-ws+1<=k):
                if s[we] in ['a','e','i','o','u']:
                    cnt+=1
                we+=1
            else:
                ans=max(ans,cnt)
                if s[ws] in ['a','e','i','o','u']:
                    cnt-=1
                ws+=1
        return ans
