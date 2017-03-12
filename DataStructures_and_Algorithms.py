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
def test():
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
# 由0或N个数据元素组成的有限序列，要记得是有顺序关系的！！！
# 重点落在：
# 1、ta是序列，有先后顺序
# 2、如果存在多个，则第一个无头，最后一个无尾，中间的有头有尾
# 3、ta是有限的
a = list("abcdefghijk")
# 上面中，b的前驱是a，b的后驱是c……
'''
    数据类型：一组性质相同的值得集合及定义在此集合上的一些操作的总称。例如整型、浮点型等等
    数据类型分为：原子类型（eg：整型、浮点型）、结构类型（eg：整数型数组）
    抽象：抽取出事物具有的普遍性的本质。eg：美女、美女王某某
    抽象数据类型：（ADT），是指一个数据模型及定义在该模型上的一组操作（类型+操作）
'''
'''
    抽象数据类型的规范化描述：
    ADT 抽象数据类型名
    Data
        数据元素之间逻辑关系的定义
    Operation
        操作
    endADT
'''
'''
    线性表的抽象数据类型
    ADT 线性表
    Data
        数据对象集合为{a1，a2，a3……an}，每个元素的类型均为datatype。其中第一个元素只有前驱，最后一个元素只有后驱
        其余元素有且只有一个前驱一个后驱。数据元素之间的关系是一对一的关系
    Operation
        1、InitList，初始化线性表
        2、ListEmpty，是否为空表
        3、ClearList，清空表
        4、GetElem，返回特定位置的元素
        5、LocateElem，查找是否有某个元素
        6、ListInsert，插入新的元素
        7、ListDelete,删除元素
        ……
    endADT
'''
# 写一个线性表的差集合，接收两个表，返回两个表的差集
def union(L1,L2):
    new_list = []
    for item in L1:
        if item not in L2:
            new_list.append(item)
    for item in L2:
        if item not in L1:
            new_list.append(item)
    return new_list
'''
输入：
a = ['a','b','c']
b = ['d','c','a']
print (union(a,b))
'''

# 写一个线性表的插入，不要用insert
def new_insert(index,loc,L1):           #写的不太好这个~~~~
    try:
        part1list = L1[:loc]
        part2list = L1[loc:]
        part1list.append(index)
        newlist = part1list + part2list
    except OverError as e:         #上面没有发生错误，所以这个地方不会有这样的情况
        print ('except:',e)        
    print ("done")
    return newlist
'''
输入：
a = list(range(10))
new_insert('hahahah',5,a)
'''

'''
线性表的存储结构：
   1、顺序存储结构（一个地址，一个值），需要：起始地址、最大存储量、当前长度
       a、读取和存储时间复杂度都是O(1)，删除和插入的时间复杂度都是O(n)
       b、优点就是快速根据位置查找元素，逻辑关系不需要增加存储空间
       c、确定就是插入和删除需要移动元素，数据量大是就不固定的消耗存储了
   2、链式存储结构（一个指针，一个地址，一个值）
       a、好特么复杂。。。。。写不下去了,和1的主要区别就是加入一个指针去指向地址的数据，而不是像1一样根据地址的连续性来
       b、查找元素，取决于i的位置，最坏的情况为O(n)
       c、核心思想是工作指针后移
       d、插入和删除就相对于顺序存储结构就差不多（在单链表上比较啊），第一次查找i位置是O(n)，之后移动指针就是O(1)了
       e、但是如果是频繁的插入和删除，单链表的优势就越来越明显。
'''



