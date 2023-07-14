class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        def dfs(node):
            if len(graph[node])==0:
                return 

            for nbr in graph[node]:
                indegmap[nbr]-=1
                if indegmap[nbr]==0:
                    dfs(nbr)


        indegmap={}
        graph=defaultdict(list)
        for i in range(numCourses):
            indegmap[i]=0

        for a,b in pre:
            graph[b].append(a)
            indegmap[a]+=1
        
        s=[]
        for k,v in indegmap.items():
            if v==0:
                s.append(k)
        
        for node in s:
            dfs(node)

        for v in indegmap.values():
            if v>0:
                return False
        return True
            
            
