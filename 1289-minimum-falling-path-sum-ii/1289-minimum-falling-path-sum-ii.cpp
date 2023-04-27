#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        vector<vector<int>> dp(grid.size(), vector<int>(grid[0].size(), -1));
        int ans = INT_MAX;
        for (int i = 0; i < grid[0].size(); i++) {
            ans = min(ans, helper(grid, dp, 0, i));
        }
        return ans;
    }
    
    int helper(vector<vector<int>>& grid, vector<vector<int>>& dp, int i, int j) {
        if (i >= grid.size() || j >= grid[0].size() || j < 0) {
            return INT_MAX;
        }
        if (dp[i][j] != -1) {
            return dp[i][j];
        }
        if (i == grid.size() - 1) {
            dp[i][j] = grid[i][j];
        } else {
            int yes = INT_MAX;
            for (int k = 0; k < grid[0].size(); k++) {
                if (k != j) {
                    int v = helper(grid, dp, i+1, k);
                    yes = min(v, yes);
                }
            }
            dp[i][j] = grid[i][j] + yes;
        }
        return dp[i][j];
    }
};
