import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class BitonicMax{
    /*
        for home work 1.4.20
    */

    public static int[] Bitonic(int N)
    {
        int mid = StdRandom.uniform(N);
        int[] a = new int[N];
        for (int i = 1; i < mid; i++) {
            a[i] = a[i-1] + 1 + StdRandom.uniform(9);
        }

        if (mid > 0) a[mid] = a[mid-1] + StdRandom.uniform(10) - 5;

        for (int i = mid + 1; i < N; i++) {
            a[i] = a[i-1] - 1 - StdRandom.uniform(9);
        }
        return a;
    }

    public static int Max(int[] a, int lo, int hi)
    {
        /*
            return array max value index
        */
        if (lo == hi) return hi;
        int mid = lo + (hi - lo) / 2;
        if(a[mid] < a[mid + 1]) return Max(a, mid + 1, hi);
        if(a[mid] > a[mid + 1]) return Max(a, lo, mid);
        else return mid;
    }

    public static void main(String[] args) {
        int[] a = BitonicMax.Bitonic(20);
        for (int i = 0; i < a.length; i++)
        {
            StdOut.println(a[i]);
        }
        int max = BitonicMax.Max(a, 0, a.length);
        StdOut.println("the max value of arrays is: " + a[max]);
    }
}