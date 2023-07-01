class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtrack(idx,arr_val):
            if idx>len(cookies):
                return float('inf')
            if idx==len(cookies):
                nonlocal ans
                ans=min(ans,max(arr_val))
                return 
            
            # print(arr_val)

            for i in range(len(arr_val)):
                arr_val[i]+=cookies[idx]
                backtrack(idx+1,arr_val)
                arr_val[i]-=cookies[idx]
                # backtrack(idx+1,arr_val)
                if arr_val[i]==0:
                    break
                #18 and 19 loc imp

        arr=[0]*k
        # print(arr)
        ans=float('inf')
        backtrack(0,arr)
        return ans