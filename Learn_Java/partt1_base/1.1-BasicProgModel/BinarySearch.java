/****************************************************************************
 *  ����:	javac -cp D:\mygit\learnJava\stdlib.jar BinarySearch.java
 *
 *  ִ��:	java -cp .;D:\mygit\learnJava\stdlib.jar BinarySearch tinyW.txt < tinyT.txt
 * 
 *  ����:	tinyW.txt
 *       	tinyT.txt
 *
 *  ���:	50
 *  	 	99
 *  	 	13
 *  
 *  ��ע���ǵ��滻���������ڵ�·��
 *
 ******************************************************************************/

import java.util.Arrays;	//��������Ŀ�

					
public class BinarySearch 
{	
	// �����Ա�ʵ�������࣬so��û��̫��
    private BinarySearch() 	
    {}
	
	// ���룺����a������key
	// ���أ�ָ��������ָ�����������������������-1
    public static int indexOf(int[] a, int key)			
    {
        int lo = 0;
        int hi = a.length - 1;
        while (lo <= hi) 
		{
			// ���ֲ��ҵ��ص�
            int mid = lo + (hi - lo) / 2;
            if      (key < a[mid]) hi = mid - 1;
            else if (key > a[mid]) lo = mid + 1;
            else return mid;
        }
        return -1;
    }

	// ��һ��@�������ڶ���Ӧ���ǵ���indexOf
    @Deprecated	
    public static int rank(int key, int[] a) 
    {
        return indexOf(a, key);
    }

	// ���������޷���
    public static void main(String[] args) 
    {
        In in = new In(args[0]);				// �����˼ҵķ��������ļ��ж�ȡ�������ŵ�whitelist������
        int[] whitelist = in.readAllInts(); 

        Arrays.sort(whitelist);					// ����
        
		while (!StdIn.isEmpty())				// ѭ������indexOf���������е�ÿ��ֵ�ҵ���Ӧ������λ��
        {
            int key = StdIn.readInt();
            if (BinarySearch.indexOf(whitelist, key) == -1)
                StdOut.println(key);
        }
    }
}