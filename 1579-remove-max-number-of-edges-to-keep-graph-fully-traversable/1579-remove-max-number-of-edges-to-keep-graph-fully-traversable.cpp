#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        vector<int> parent(n+1);
        vector<int> rank(n+1);
        for(int i=1;i<=n;i++){
            parent[i]=i;
            rank[i]=0;
        }
        int alice_edge=0;
        int bob_edge=0;
        int ans=0;
        for(auto edge:edges){
            if(edge[0]==3){
                int p1=find(edge[1],parent);
                int p2=find(edge[2],parent);
                if(p1!=p2){
                    union_set(edge[1],edge[2],parent,rank);
                    alice_edge++;
                    bob_edge++;
                }
                else{
                    ans++;
                }
            }
        }
        vector<int> alice_dsu=parent;
        vector<int> alice_rank=rank;
        vector<int> bob_dsu=parent;
        vector<int> bob_rank=rank;
        for(auto edge:edges){
            if(edge[0]==1){
                int p1=find(edge[1],alice_dsu);
                int p2=find(edge[2],alice_dsu);
                if(p1!=p2){
                    union_set(edge[1],edge[2],alice_dsu,alice_rank);
                    alice_edge++;
                }
                else{
                    ans++;
                }
            }
            else if(edge[0]==2){
                int p1=find(edge[1],bob_dsu);
                int p2=find(edge[2],bob_dsu);
                if(p1!=p2){
                    union_set(edge[1],edge[2],bob_dsu,bob_rank);
                    bob_edge++;
                }
                else{
                    ans++;
                }
            }
        }
        if(alice_edge!=n-1 || bob_edge!=n-1){
            return -1;
        }
        return ans;
    }
private:
    int find(int u,vector<int>& parent){
        if(parent[u]!=u){
            parent[u]=find(parent[u],parent);
        }
        return parent[u];
    }
    void union_set(int u,int v,vector<int>& parent,vector<int>& rank){
        int p1=find(u,parent);
        int p2=find(v,parent);
        if(p1!=p2){
            if(rank[p1]>rank[p2]){
                parent[p2]=p1;
            }
            else if(rank[p2]>rank[p1]){
                parent[p1]=p2;
            }
            else{
                parent[p1]=p2;
                rank[p2]+=1;
            }
        }
    }
};
