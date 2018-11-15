class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        perimeter = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    perimeter += self.getCellPerimeter(i, j, grid)

        return perimeter

    def getCellPerimeter(self, i, j, grid):
        cellPerimeter = 0
        # print(i, j)

        if (i - 1 < 0) or (grid[i - 1][j] == 0):
            cellPerimeter += 1

        if (i + 1 == self.m) or (grid[i + 1][j] == 0):
            cellPerimeter += 1

        if (j - 1 < 0) or (grid[i][j - 1] == 0):
            cellPerimeter += 1

        if (j + 1 == self.n) or (grid[i][j + 1] == 0):
            cellPerimeter += 1

        return cellPerimeter

    def islandPerimeter2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        this another solution
        """
        self.grid = grid
        self.m = len(self.grid)
        self.n = len(self.grid[0])

        start = [-1, -1]
        for i in range(self.m + 1):
            for j in range(self.n + 1):
                if self.lowerRightIsLand(i, j):
                    start = [i, j]
                    current = [i, j]
                    break
            if start[0] != -1:
                break

        perimeter = 0
        while(True):
            print("current: ({0},{1})".format(current[0], current[1]))
            # 向右
            if self.lowerRightIsLand(current[0], current[1]):
                current[1] += 1
                perimeter += 1
            # 向下
            elif self.lowerLeftIsLand(current[0], current[1]):
                current[0] += 1
                perimeter += 1
            # 向左
            elif self.upperLeftIsLand(current[0], current[1]):
                current[1] -= 1
                perimeter += 1
            # 向上
            elif self.upperRightIsLand(current[0], current[1]):
                current[0] -= 1
                perimeter += 1
            else:
                raise Exception("({0}) error!".format(current))

            if current[0] == start[0] and current[1] == start[1]:
                break

        return perimeter

    def lowerRightIsLand(self, i, j):
        # can turn right?
        if j < self.n and i < self.m and self.grid[i][j] == 1:
            # turn right is legal?
            if i > 0 and self.grid[i-1][j] + self.grid[i][j] == 2:
                return False
            return True
        return False

    def lowerLeftIsLand(self, i, j):
        # can turn down?
        if j > 0 and i < self.m and self.grid[i][j-1] == 1:
            # turn down is legal?
            if j < self.n and self.grid[i][j] + self.grid[i][j-1] == 2:
                return False
            return True
        return False

    def upperRightIsLand(self, i, j):
        # can turn up?
        if j < self.n and i > 0 and self.grid[i-1][j] == 1:
            # turn up is legal?
            if j > 0 and self.grid[i-1][j-1] + self.grid[i-1][j] == 2:
                return False
            return True
        return False

    def upperLeftIsLand(self, i, j):
        # can turn left?
        if j > 0 and i > 0 and self.grid[i-1][j-1] == 1:
            # turn left is legal?
            if i < self.m and self.grid[i-1][j-1] + self.grid[i][j-1] == 2:
                return False
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(s.islandPerimeter(grid))
