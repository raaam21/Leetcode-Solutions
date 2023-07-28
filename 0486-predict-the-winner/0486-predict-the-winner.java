class Solution {
    public int solve(int left, int right,int[] nums){
        if (left==right) {
            return nums[left];
        }
            
        int l=nums[left]-solve(left+1,right,nums);
        int r=nums[right]-solve(left,right-1,nums);
        return Math.max(l,r);
    
    }
    public boolean PredictTheWinner(int[] nums) {
        return solve(0,nums.length-1,nums)>=0;
        
    }
}