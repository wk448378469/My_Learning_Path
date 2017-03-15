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
    except IndexError as e:         #上面没有发生错误，所以这个地方不会有这样的情况
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
       d、插入和删除就相对于顺序存储结构就差不多（和单链表上比较啊），第一次查找i位置是O(n)，之后移动指针就是O(1)了
       e、但是如果是频繁的插入和删除，单链表的优势就越来越明显。
'''
# 创建一个线性表的链式存储结构（用python来实现的）
class Sqlist(object):
    def __init__(self,size):
        self.data = list(None for _ in range(size))
        self.lenth = 0
        self.max_size = size
    
    def add_item(self,item):        #添加单个item
        if self.lenth < self.max_size:
            self.data[self.lenth] = item
            self.lenth = self.lenth + 1
        else:
            raise IndexError ("List is full")
    
    def create_list(self,tar_list):    #添加一个list到线性表中
        for i,item in enumerate(tar_list):
            if self.lenth >= self.max_size:
                raise IndexError ("List is full")
            else:
                self.add_item(tar_list[i])
    
    def delete(self,i):     #删除节点中某个值
        if i >self.lenth or i < 0:
            raise IndexError ("Index out of range")
        else:
            j = i
            while j < self.lenth:
                self.data[j-1] = self.data[j]
                j = j + 1
            self.data[self.lenth - 1] = None
            self.lenth = self.lenth -1
    
    def get_elem(self,i):           #查找表中的某个值
        if i > self.lenth or i < 0:
            raise IndexError ("Index out of range")
        else:
            return self.data[i-1]
        
    def get_location(self,elem):    # 返回第一个节点为elem的位置
        for i , item in enumerate(self.data):
            if item == elem:
                return i + 1
            return -1
    
    def show_list(self):          #返回所有元素
        for i , item in enumerate(self.data):
            if item is not None:
                print (self.data[i])
            else:
                print (' ')
                break
'''
输入：
if __name__ == '__main__':
    sql = Sqlist(10)
    ll = [1,2,3,4,5]
    sql.create_list(ll)
    sql.show_list()
    sql.delete(1)
    sql.show_list()
    sql.get_elem(4)
    b = sql.get_location(3)
    print (b)
'''

'''
    单链表结构与顺序存储结构的优缺点对比（分配方式、时间性能、空间性能）：
    A、分配方式
        顺序存储结构用一段连续的存储单元依次存储数据元素
        单链表采用链式存储结构，用一组任意的存储单元存储数据元素
    B、时间性能
        1、查找：
            顺序存储结构，O(1)
            单链表，O(n)
        2、插入和删除
            顺序存储结构，O(n)
            单链表，O(1)
    C、空间性能
        顺序存储结构需要预先分配存储空间，当然貌似现在也有动态分配存储空间的优化了
        单链表不需要分配，只要有就好
    
    so，不同的应用场景用不同的吧~~~
'''

'''
    一种特殊的链式结构——静态链表
    理解起来就是古人们（汇编语言上面的吧可能）没有链式结构的时候用两个数组（顺序存储的）组成一个静态链表，其中一个数组存放指针一个存放数据.....
    @_@ 聪明啊
'''

'''
    例题：快速查找未知长度单链表的中间节点
    anwser1：全部遍历一遍，然后算出长度后，在找到L/2位置的值，O(L+L/2) = O(3L/2)
    anwser2：利用快慢指针来，设快指针一次跨两个，慢指针一次跨一个，当快指针遍历完后，慢指针刚好完成。O(2/L),快上三倍！！！
'''

# 循环链表~~~
# 单链表只能向后，不能向前~所以就是单链表最后的指针不要指向空，而是指向到单链表的头就可以了
# 实在是没写出来。。。很尴尬~~~

# 约瑟夫问题
# 41个人，第一个人开始报数，数到3这个人就自杀，后面的人继续从一开始，剩下两个人就不用自杀了，问站在那个位置可以跑路不自杀~
# 抽象出问题就是，已知n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。从编号为k的人开始报数，数到k的那个人被杀掉；他的下一个人又从1开始报数，数到k的那个人又被杀掉；依此规律重复下去，直到圆桌周围的人只剩最后一个。
# 思路是：当k是1的时候，存活的是最后一个人，当k>=2的时候，构造一个n个元素的循环链表，然后依次杀掉第k个人，留下的最后一个或两个是可以存活的人 
def Joseph(n,k):
    if k == 1:
        print ('survive:',n)
        return 
    p = 0      #用来标记列表位置用的
    people = list(range(1,n+1))      # range函数不包括stop，所以要n+1
    while True:
        if len(people) == 1:
            break
        p = (p + (k - 1))%len(people)      #取余数的时候，如果被除数小于除数则，结果为被除数！！！涨知识了@_@
        print ('kill:',people[p])
        del people[p]
    print ('survive:',people[0])

'''
输入：
if __name__ == '__main__':
    Joseph(10,4)
    Joseph(11,4)
    Joseph(20,5)
'''
#还有其他两个问题，诸如魔术师发牌问题、拉丁方阵问题等....太难了就不写了吧

# 双向循环链表，类似于火车。。。有两个头
def move(n):
    if type(n) != int:
        print ("wrong input")
    if n>25:
        n = n%25
    a = list('abcdefghijklmnopqrstuvwxyz')
    part1list = a[:n]
    part2list = a[n:]
    newlist = a[n:]+a[:n]
    return newlist
#感觉比课程中的c语言简单多了....


# part5 栈和队列！！
# 栈是线性表的一种具体表现，是非常重要的线性结构。
# “后进先出” 就想手枪的子弹、或者像浏览器的后退按钮、或者像ps或axure的撤销操作
# 只能在表尾部进行删除或插入的操作
# 对于栈的表尾称为栈顶，表头称为栈底

# 栈的插入，叫做push，进栈、压栈、入栈
# 栈的删除，叫做pop，出栈、弹栈
# 栈因为是一个线性表，所以也分为顺序存储结构和链式存储结构
stack = [3,4,5]
stack.append(6)     #进栈
stack.pop()         #出栈
#。。。这么写是不是有点不专业....
class Stack(object):
    def __init__(self,size):
        self.size = size
        self.stack = []
    
    def __str__(self):
        return str(self.stack)
    
    def getSize(self):
        return len(self.stack)
    
    def push(self,x):
        # 入栈
        if self.isfull():
            raise Exception("满了别塞了")
        self.stack.append(x)
    
    def pop(self):
        # 出栈
        if len(self.stack) == 0:
            raise Exception("大哥是空的")
        return self.stack.pop()
    
    def isfull(self):
        if len(self.stack) == self.size:
            return True
        else:
            return False

# 就这样吧，测试一下
'''
if __name__ == '__main__':
    stackTest = Stack(10)
    for i in range(10):
        stackTest.push(i)
    print (stackTest.getSize())
    print (stackTest.isfull())
    print (stackTest)
    
    for i in range(6):
        stackTest.pop()
    
    print (stackTest.getSize())
'''
# 在C语言里面呢，指针是指向地址的，地址呢又可以为空，所以这里其实有两种方法
# 方法一呢就是top指针指向最后面一个带有内容的地址
# 方法二呢就是top指针指向最后面一个带有内容的地址+1，理解起来就是指针永远在最后内容的后面一个，这样子可能更贴近实际的"栈"的定义吧
# 上面的代码里面可能包含了出栈、入栈，其实还可以有清空栈L[:] = []，销毁栈....不知道怎么写,__del__(self)??

# 栈的链式存储结构~，，，，知识点了解下得了。。。。
# 栈的应用
# 逆波兰表达式又称为后缀表达式....大致的意思就是(1-2)*(4+5)这样的中表缀达式呢，人一看就懂，也能快速算出来结果是-9
# 但是计算机不喜欢这样的，因为需要很多的if来判断哪个要先计算哪个要后计算。。。所以有一天一个伟人想出来了。。。f***
# 所以上面的用逆波兰表达式来就是：1 2 - 4 5 + * 。。。。鬼tm才能懂
# 大致的意思就是，遇到数字就进栈，遇到运算符就出栈
# 翻译一下就是：1和2先进栈，遇到-做减法，1和2出栈做减法，然后-1进栈，然后4和5进栈，然后遇到+做加法，4和5出栈做加法，然后9进栈，遇到* 则 1和-9出栈做乘法，然后-9不进栈！！！，最后返回-9和空栈
# 所以做一下？？？？
def nblbds(exp):
    stack = []
    for val in exp:
        if val in ['+','-','*','/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if val == '-':
                result = op2 - op1
            if val == '+':
                result = op2 + op1
            if val =='*':
                result = op2 * op1
            if val =='/':
                result = op2 / op1
            stack.append(result)
        else:
            stack.append(int(val))
    return stack.pop()
'''
输入:
if __name__ == '__main__':
    exp = '12-45+*'
    print (nblbds(exp))
这是一个后缀表达式输入，输出结构的方法
'''

# 如果是输入中缀表达式，转化为后缀表达式，然后再计算呢？比如输入一个：1+（2-3）*4+10/2呢？
# 所以写一个中缀表达式转后缀表达式的方法，然后在调用上面的nblbds方法就可以了~
'''
    这里的问题有两个：
    1、当遇到右括号时，要把做到左括号的之间的其他符号输出，因为括号的优先级最高嘛
    2、当栈顶的符号为乘除时，入栈的符号如果是加减，则需要先把乘除出栈，输出，然后把乘除前的加减也输出，然后新的加减入栈
'''
def in2hind(inexp):
    stack = []
    for val in inexp:
        if val.isdigit():             # 是否是数字
        if val == ')':
            
    return str(stack)

# part6 队列
# 队列，只允许在一段进行插入，另一端进行删除操作的线性表。先进先出~
# 就类似于排队上车~
# 对头呢出队列，对尾部入队列
# 和栈另一个不同点就是，栈一般用顺序结构来实现，但是队列一般用链式结构来实现，所以就叫做链队列
# 其实也很理解就是用链式结构来标记头尾
# 所以重要的是出队列和进队列的操作，写一个？
# 另外说一句，就是python的列表这个数据结构，我感觉就是包含了顺序结构和链式结构的，可能这就是高级语言简单的地方吧....
# 循环队列，就是不断根据入队或出队，调整头指针和尾指针的位置
# 好准备写一个吧