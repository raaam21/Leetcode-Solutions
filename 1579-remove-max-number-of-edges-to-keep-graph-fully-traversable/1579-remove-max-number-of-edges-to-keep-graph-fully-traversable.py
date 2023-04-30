class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(u,parent):
            if parent[u]!=u:
                parent[u]=find(parent[u],parent)
            return parent[u]

        def union(u,v,parent,rank):
            p1=find(u,parent)
            p2=find(v,parent)
            

            if p1!=p2:
                if rank[p1]>rank[p2]:
                    parent[p2]=p1
                
                elif rank[p2]>rank[p1]:
                    parent[p1]=p2
                else:
                    parent[p1]=p2
                    rank[p2]+=1
            
            


        parent=[i for i in range(n+1)]
        rank=[0 for i in range(n+1)]
        edges.sort(key=lambda x:x[0],reverse=True)
    
        alice_edge=0
        bob_edge=0
        ans=0
        
        for typed,u,v in edges:
            if typed==3:
                p1=find(u,parent)
                p2=find(v,parent)
                if p1!=p2:
                    union(u,v,parent,rank)
                    alice_edge+=1
                    bob_edge+=1
                else:
                    ans+=1
        
        alice_dsu=parent.copy()
        alice_rank=rank.copy()
        bob_dsu=parent.copy()
        bob_rank=rank.copy()

        for typed,u,v in edges:
            if typed==2:
                p1=find(u,bob_dsu)
                p2=find(v,bob_dsu)
                if p1!=p2:
                    union(u,v,bob_dsu,bob_rank)
                    bob_edge+=1
                else:
                    ans+=1

            if typed==1:
                p1=find(u,alice_dsu)
                p2=find(v,alice_dsu)
                if p1!=p2:
                    union(u,v,alice_dsu,alice_rank)
                    alice_edge+=1
                else:
                    ans+=1
        if alice_edge==bob_edge==n-1:
            return ans
        return -1