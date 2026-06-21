class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lr_pro, rl_pro = [], []

        i, j = 0, len(nums) - 1

        lr, rl = 1, 1

        while i < len(nums):
            lr *= nums[i]
            rl *= nums[j]
            
            lr_pro.append(lr)
            rl_pro.append(rl)

            i += 1
            j -= 1
            
        rl_pro = rl_pro[::-1]
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(rl_pro[i + 1])
            elif i == len(nums) - 1:
                res.append(lr_pro[i - 1])
            else:
                res.append(lr_pro[i - 1] * rl_pro[i + 1])
        
        return res


        