import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

public class MergeSortImprove
{

    /* 
        homework: 2.2.11
            1 speeding up the sorting of small array
            2 whether the test has been sorted
            3 exchange parameters
    */

    private static final int cutoff = 7;

    private static void merge(Comparable[] a, Comparable[] aux, int lo, int mid, int hi)
    {
        int i = lo;              // left index
        int j = mid + 1;         // right index
        for( int k = lo; k <= hi; k++)
        {
            if      (i > mid)                   aux[k] = a[j++];
            else if (j > hi)                    aux[k] = a[i++];
            else if (less(a[j], a[i]))          aux[k] = a[j++];
            else                                aux[k] = a[i++];
        }
    }

    private static void sort(Comparable[] a, Comparable[] aux, int lo, int hi)
    {
        if (hi <= lo + cutoff)
        {
            //1 speeding up the sorting of small array
            insertionSort(aux, lo, hi);
            return;
        }

        int mid = lo + (hi - lo) / 2;

        //3 exchange parameters
        sort(aux, a, lo, mid);
        sort(aux, a, mid+1, hi);

        if (!less(a[mid+1], a[mid]))
        {
            //2 whether the test has been sorted
            for (int i = lo; i <= hi; i++) 
            {
                aux[i] = a[i];
            }
        }

        merge(a, aux, lo, mid, hi);
    }

    public static void sort(Comparable[] a)
    {
        Comparable[] aux = a.clone();
        sort(aux, a, 0, a.length - 1);
    }

    private static boolean less(Comparable v, Comparable w)
    {
        return v.compareTo(w) < 0;
    }

    private static void exch(Comparable[] a, int i, int j) {
        Comparable swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }

    private static void insertionSort(Comparable[] a, int lo, int hi) {
        for (int i = lo; i <= hi; i++)
            for (int j = i; j > lo && less(a[j], a[j-1]); j--)
                exch(a, j, j-1);
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
