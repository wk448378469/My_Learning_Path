# 数据结构和算法

# part1 数据结构的初体验
# 数据结构分为逻辑结构和物理结构
# 逻辑结构分为：集合结构、线性结构、树形结构、图形结构
# 物理结构中存储结构形式有顺序存储（类似于排队）和链式存储（类似于银行取号）

# part2 算法的初体验
# 计算1+2+3+……+99+100

def sum1():
    #程序思维
	i = 1
	sum = 0
	while i<= 100:
		sum = sum + i
		i = i +1
	return sum 

def sum2():
    #算法思维，等差求和
    i = 100 
    sum = (1 + i)*i/2
    return sum
        
# 对比上面两个函数就会发现，sum1函数需要循环一百次，sum2则只需要执行一次即可。如果把i扩大到10000W就可以看出那个更好了。
if __name__ =='__main__':
    from timeit import Timer
    t1 = Timer("sum1","from __main__ import sum1")
    t2 = Timer("sum2","from __main__ import sum2")
    print (t1.timeit(100000000))
    print (t2.timeit(100000000))

# 通过以上可以测试出sum2比sum1 相对来说快那么一些~
# 算法的五个基本特征：输入、输出、有穷性、确定性、可行性

# part3 算法效率的度量方法
# 比较两个算法时，可以假设两个算法的输入规模都是N，算法A要做2N+3次核心操作（剔除掉赋值和打印等其他的），算法B要做3N+1次操作
# 比较刚刚两个算法哪个更快一些
def which_fast1():
    N = 1       # 输入规模
    while N<100:  
        alA = 2*N + 3    #算法一执行次数
        alB = 3*N + 1    #算法二执行次数   
        if alA < alB:
            print ("算法A执行次数小于算法B,输入规模为",N)
            N = N + 1
        elif alA == alB:
            print ("算法A执行次数等于算法B,输入规模为",N)
            N = N + 1
        else:
            print ("算法A执行次数大于算法B,输入规模为",N)
            N = N + 1
# 当输入次数小于2时A快，当输入次数等于2时AB一样快，当输入次数大于2时B快
# 常数项基本不会影响到后来基本上

# 假设两个算法的输入规模都是N，算法A要做4N+8次核心操作，算法B要做2N*N+1次操作呢？
def which_fast2():
    N = 1       # 输入规模
    while N<100:  
        alA = 4*N + 8    #算法一执行次数
        alB = 2*N*N + 1    #算法二执行次数   
        if alA < alB:
            print ("算法A执行次数小于算法B,输入规模为",N)
            N = N + 1
        elif alA == alB:
            print ("算法A执行次数等于算法B,输入规模为",N)
            N = N + 1
        else:
            print ("算法A执行次数大于算法B,输入规模为",N)
            N = N + 1

# A永远都小于B，因为B是平方的
# 所以关注点在于：最高次项的指数大，增长的就快（算得多），最高次项的系数次之，常数项次次之。

# 时间复杂度和空间复杂度呢？
# 时间复杂度：执行次数T(n)是问题规模n的函数，进而分析执行次数T(n)随n的变化情况并确定T(n)的数量级
# 记为：T(n) = O(f(n)) ，重点是关注增长率！！！所以最高项阶数最重要，其他都忽略~
def Constant_order():
    sum = 0
    n = 100
    print ("hahahahha")
    print ("hahaha")
# 上面的函数中，O几呢？其实就是O(1)就可以，不用写成O(4)
#上面的是常数阶，就是固定的语句不会受上面输入项而改变

def Linear_order(n):
    while n < 100:
        print (n)
        n = n + 1
    print ("over")
    print ("true over")
# 上面这个就是线性阶，f(n) = 2n + 2，所以时间复杂度就是O(n)
# 当然还有就是平方阶，时间复杂度就是O(n^2),x就是2的几次幂
# 居然还TM有是对数阶，时间复杂度就是O(logn)
# 居然还有...nlogn阶，O(nlogn) 
# 还有...立方阶，O(n^3)
# 还有...指数阶，O(2^n)
# 所以他们的顺序是O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(n^3)<O(2^n)<O(n!)<O(n^n)

# 空间复杂度就是n所占存储空间的函数啦~
# 记为：S(n) = O(f(n))


# part 4 线性表




                    