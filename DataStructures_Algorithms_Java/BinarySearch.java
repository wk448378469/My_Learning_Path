import java.util.Arrays;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class BinarySearch
{
    public static int rank(int key, int[] a)
    {
        int lo = 0;
        int hi = a.length - 1;
        while (lo <= hi)
        {
            int mid = lo + (hi - lo) / 2;
            if      (key < a[mid]) { hi = mid - 1;}
            else if (key > a[mid]) { lo = mid + 1;}
            else                   { return mid;}
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] whiteList = In.readInts(args[0]); // read a file as white list
        Arrays.sort(whiteList);
        while (!StdIn.isEmpty())
        {
            int key = StdIn.readInt();     // from a file read a int as key
            if ( rank(key, whiteList) <0)
            {
                StdOut.println(key);
            }
        }
    }
}