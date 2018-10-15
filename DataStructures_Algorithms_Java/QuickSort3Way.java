import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class QuickSort3Way
{

    /* 
        quick sort 3 way:  time complexity is about O(N * lgN)

        this is a solution to a large number of equal elements.
    */

    private static void sort(Comparable[] a, int lo, int hi)
    {
        if( hi <= lo) return;

        int lt = lo;               // left index
        int i = lo + 1;
        int gt = hi;                // right index
        Comparable v = a[lo];
        while(i <= gt)
        {
            int cmp = a[i].compareTo(v);
            if      (cmp < 0)   exch(a, lt++, i++);
            else if (cmp > 0)   exch(a, i, gt--);
            else                i++;
        }
        sort(a, lo, lt - 1);
        sort(a, gt+ 1, hi);
    }

    public static void sort(Comparable[] a)
    {
        StdRandom.shuffle(a);
        sort(a, 0, a.length - 1);
    }

    private static boolean less(Comparable v, Comparable w)
    {
        return v.compareTo(w) < 0;
    }

    private static void exch(Comparable[] a, int i, int j)
    {
        Comparable t = a[i];
        a[i] = a[j];
        a[j] = t;
    }

    private static void show(Comparable[] a)
    {
        for(int i = 0; i < a.length; i++)
        {
            StdOut.print(a[i] + " ");
        }
        StdOut.println();
    }

    public static boolean isSorted(Comparable[] a, int lo, int hi)
    {
        for(int i = lo; i <= hi; i++)
        {
            if( less(a[i], a[i-1])) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        String[] a = In.readStrings();
        sort(a);
        assert isSorted(a, 0, a.length);
        show(a);
    }
}
