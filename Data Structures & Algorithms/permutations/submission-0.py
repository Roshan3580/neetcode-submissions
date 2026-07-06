class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        done = [False]*len(nums)
        
        def dfs(curr, nums, done):
            if len(nums) == len(curr):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if done[i] == False:
                    done[i] = True
                    curr.append(nums[i])
                    dfs(curr, nums, done)
                    done[i] = False
                    curr.pop()

        dfs([], nums, done)
        return res
