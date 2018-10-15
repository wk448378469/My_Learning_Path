import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

public class HeapSort
{

    /* 
        heap sort:  time complexity is about O(N * lgN)
    */

    public static void sort(Comparable[] pq)
    {
        int n = pq.length;
        for (int k = n / 2; k >= 1; k--)
            sink(pq, k, n);

        while( n > 1)
        {
            exch(pq, 1, n--);
            sink(pq, 1, n);
        }
    }

    private static void sink(Comparable[] pq, int k, int n)
    {
        while(2*k <= n)
        {
            int j = 2*k;
            if (j < n && less(pq, j, j+1)) j++;
            if ( !less(pq, k, j)) break;
            exch(pq, k, j);
            k = j;
        }
    }

    private static boolean less(Comparable[] pq, int i, int j)
    {
        return pq[i-1].compareTo(pq[j-1]) < 0;
    }

    private static void exch(Comparable[] pq, int i, int j)
    {
        Comparable swap = pq[i-1];
        pq[i-1] = pq[j-1];
        pq[j-1] = swap;
    }

    private static void show(Comparable[] a) {
        for (int i = 0; i < a.length; i++) {
            StdOut.println(a[i]);
        }
    }

    public static boolean isSorted(Comparable[] a)
    {
        for(int i = 1; i < a.length; i++)
        {
            if( less(a, i, i-1)) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        String[] a = In.readStrings();
        sort(a);
        assert isSorted(a);
        show(a);
    }
}
