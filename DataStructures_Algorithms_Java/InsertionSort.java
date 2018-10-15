import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

public class InsertionSort
{

    /* 
        insert sort:  time complexity is about O(N**2 / 4)
    */

    public static void sort(Comparable[] a)
    {
        int N = a.length;
        for( int i = 0; i < N; i++)
        {
            for( int j = i; j > 0; j--)
            {
                if (less(a[j], a[j-1])) exch(a, j, j-1);
                else break;
            }

        }
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

    public static boolean isSorted(Comparable[] a)
    {
        for(int i = 1; i < a.length; i++)
        {
            if( less(a[i], a[i-1])) return false;
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
