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
