class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        curr_max,curr_min,ans=nums[0],nums[0],nums[0]
        
        for i in range(1,n):
            # swap if negative
            if nums[i]<0:
                curr_max,curr_min=curr_min,curr_max
            curr_max=max(nums[i],curr_max*nums[i])
            curr_min=min(nums[i],curr_min*nums[i])
            ans=max(ans,curr_max)

        return ans
        
