class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict = {}
        for index, num in enumerate(nums):
            another = target - num
            if another in mydict:
                return (mydict.get(another), index)
            mydict[num] = index


if __name__ == '__main__':
    solution = Solution()
    result = solution.twoSum([2, 10, 1, 9, 7, 32], 17)
    print(result)
