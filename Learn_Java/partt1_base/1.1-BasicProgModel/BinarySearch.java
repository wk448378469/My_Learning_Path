/****************************************************************************
 *  编译:	javac -cp D:\mygit\learnJava\stdlib.jar BinarySearch.java
 *
 *  执行:	java -cp .;D:\mygit\learnJava\stdlib.jar BinarySearch tinyW.txt < tinyT.txt
 * 
 *  数据:	tinyW.txt
 *       	tinyT.txt
 *
 *  输出:	50
 *  	 	99
 *  	 	13
 *  
 *  备注：记得替换两个包所在的路径
 *
 ******************************************************************************/

import java.util.Arrays;	//导入数组的库

					
public class BinarySearch 
{	
	// 不可以被实例化的类，so，没搞太懂
    private BinarySearch() 	
    {}
	
	// 输入：数组a、整数key
	// 返回：指定数组中指定键的索引，特殊情况返回-1
    public static int indexOf(int[] a, int key)			
    {
        int lo = 0;
        int hi = a.length - 1;
        while (lo <= hi) 
		{
			// 二分查找的重点
            int mid = lo + (hi - lo) / 2;
            if      (key < a[mid]) hi = mid - 1;
            else if (key > a[mid]) lo = mid + 1;
            else return mid;
        }
        return -1;
    }

	// 第一个@不懂，第二个应该是调用indexOf
    @Deprecated	
    public static int rank(int key, int[] a) 
    {
        return indexOf(a, key);
    }

	// 主方法，无返回
    public static void main(String[] args) 
    {
        In in = new In(args[0]);				// 调用人家的方法，从文件中读取整数，放到whitelist数组中
        int[] whitelist = in.readAllInts(); 

        Arrays.sort(whitelist);					// 排序
        
		while (!StdIn.isEmpty())				// 循环调用indexOf，给数组中的每个值找到对应的索引位置
        {
            int key = StdIn.readInt();
            if (BinarySearch.indexOf(whitelist, key) == -1)
                StdOut.println(key);
        }
    }
}