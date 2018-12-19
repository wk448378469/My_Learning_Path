from functools import cmp_to_key
from itertools import zip_longest

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        result = "".join(sorted(map(str, nums), key=LargerNumKey))
        return result if result[0] != 0 else "0"

if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([3,30,34,5,9]))
