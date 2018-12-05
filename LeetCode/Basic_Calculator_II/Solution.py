class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals, num, sign = [], 0, "+"
        length = len(s)
        for i in range(length):
            if s[i].isdigit():
                num = num*10 + ord(s[i]) - ord("0")
            if not s[i].isdigit() and not s[i].isspace() or i == length-1:
                if sign == "-":
                    vals.append(-num)
                elif sign == "+":
                    vals.append(num)
                elif sign == "*":
                    vals.append(vals.pop() * num)
                else:
                    temp = vals.pop()
                    if temp//num < 0 and temp % num != 0:
                        vals.append(temp // num+1)
                    else:
                        vals.append(temp // num)
                sign = s[i]
                num = 0
        return sum(vals)

if __name__ == '__main__':
    s = Solution()
    print(s.calculate("14-3/2"))
