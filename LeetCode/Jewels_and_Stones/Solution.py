class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(s in set(J) for s in S)


if __name__ == '__main__':
    s = Solution()
    print(s.numJewelsInStones("aA", "aAAbbbaSDAIHSDOAb"))
