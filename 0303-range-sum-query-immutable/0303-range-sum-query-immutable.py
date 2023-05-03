class NumArray:

    def __init__(self, nums: List[int]):
        self.ps=[]
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            self.ps.append(s)
        print(self.ps)

    def sumRange(self, left: int, right: int) -> int:
        if left>0:
            return(self.ps[right]-self.ps[left-1])
        return self.ps[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)