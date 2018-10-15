import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

public class MergeSortX
{

    /* 
        home work: 2.2.10
        use descending order copy to aux
    */

    private static void merge(Comparable[] a, Comparable[] aux, int lo, int mid, int hi)
    {
        assert isSorted(a, lo, mid);
        assert isSorted(a, mid+1, hi);

        for (int k = lo; k <= mid; k++) 
            aux[k] = a[k];
        for (int k = mid + 1; k <= hi; k++)
            aux[k] = a[k];

        int i = lo;
        int j = hi;

        for (int k = lo; k <= hi; k++)
        {
            if (less(aux[j],aux[i]))    a[k] = aux[j--];
            else                        a[k] = aux[i++];
        }
    }

    private static void sort(Comparable[] a, Comparable[] aux, int lo, int hi)
    {
        if ( hi <= lo) return;
        int mid = lo + (hi - lo) / 2;
        sort(a, aux, lo, mid);
        sort(a, aux, mid+1, hi);
        if ( !less(a[mid+1], a[mid])) return;
        merge(a, aux, lo, mid, hi);
    }

    public static void sort(Comparable[] a)
    {
        Comparable[] aux = new Comparable[a.length];
        sort(a, aux, 0, a.length - 1);
    }

    private static boolean less(Comparable v, Comparable w)
    {
        return v.compareTo(w) < 0;
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
