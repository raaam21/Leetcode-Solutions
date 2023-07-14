class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # cycle detection algo 

        def dfs(node):
            vis[node]=True
            pvis[node]=True
            notsafestate[node]=False
            for nbr in graph[node]:
                if vis[nbr]==False:
                    if dfs(nbr)==True:
                        notsafestate[node]=True
                        return True
                elif vis[nbr] and pvis[nbr]==True:
                    notsafestate[node]=True
                    return True

            pvis[node]=False
            return False


        vis=[False for i in range(len(graph))]
        notsafestate=[True for i in range(len(graph))]
        pvis=[False for i in range(len(graph))]
        
        for i in range(len(graph)):
            if vis[i]==False:
                dfs(i)
        print(notsafestate)
        ans=[]
        for i in range(len(notsafestate)):
            if notsafestate[i]==False:
                ans.append(i)

        return ans
