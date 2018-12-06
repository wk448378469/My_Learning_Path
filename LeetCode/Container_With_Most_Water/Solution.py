class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea, lo, hi = 0, 0, len(height) - 1
        while(lo < hi):
            temp = min(height[hi], height[lo]) * (hi - lo)
            if temp > maxArea:
                maxArea = temp

            if height[hi] > height[lo]:
                lo += 1
            else:
                hi -= 1

        return maxArea


if __name__ == '__main__':
    s = Solution()
    h = [2, 3, 10, 5, 7, 8, 9]
    result = s.maxArea(h)
    print(result)
