class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        def find(u):
            if parent[u]!=u:
                parent[u]=find(parent[u])
            return parent[u]

        def union(u,v):
            p1=find(u)
            p2=find(v)

            if p1!=p2:
                if rank[p1]>rank[p2]:
                    parent[p2]=p1
                
                elif rank[p2]>rank[p1]:
                    parent[p1]=p2
                else:
                    parent[p1]=p2
                    rank[p1]+=1


        graph=defaultdict(list)
        # a to b weight c
        for i in range(len(queries)):
            queries[i].append(i)
        
        parent=[i for i in range(n)]
        rank=[0 for i in range(n)]

        queries.sort(key=lambda x:x[2])
        edgeList.sort(key=lambda x:x[2])
        print(edgeList)

        ans=[False for i in range(len(queries))]
        i=0
        for u,v,lim,idx in queries:
            while(i<len(edgeList) and edgeList[i][2]<lim):
                union(edgeList[i][0],edgeList[i][1])
                i+=1
            if(find(u)==find(v)):
                ans[idx]=True
            
        
        return ans
         