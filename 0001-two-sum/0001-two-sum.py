class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s=0
        c=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if((nums[i]+nums[j])==target):
                    c.append(i)
                    c.append(j)
                else:
                    continue
            if(len(c)>0):
                break
        return (c)
                


