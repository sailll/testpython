class Solution(object):
    def firstMissingPositive(self, nums):
        a=dict()
        for i in range(len(nums)):
            if(nums[i]>0):
                a[nums[i]]=1
        c=1
        b=sorted(a.keys());
        for i in b:
            if(i!=c):
                return c
            c=c+1
        return c
        """
        :type nums: List[int]
        :rtype: int
        """
        