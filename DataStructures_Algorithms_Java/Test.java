import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdRandom;
import java.util.HashMap;
import java.util.Map;


public class Test
{
    private final int month;
    private final int day;
    private final int year;

    public Test(int m, int d, int y){ month = m; day = d; year = y;}
    public int month(){ return month;}
    public int day(){ return day;}
    public int year() { return year;}
    public String toString(){ return month() + "/" + day() + "/" + year();}

    public boolean equals(Object x)
    {
        if (this == x) return true;
        if (x == null) return false;
        if (this.getClass() != x.getClass()) return false;
        Test that = (Test) x;
        if (this.year != that.year) return false;
        if (this.month != that.month) return false;
        if (this.day != that.day) return false;
        return true;
    }

    public static void main(String[] args) {
        int a = 1;
        int b = 3;
        StdOut.println((float) a / b);
    }
}