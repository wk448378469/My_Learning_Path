import edu.princeton.cs.algs4.StdOut;

public class Stopwatch{

    /*
        this is a timer class
        when init, timer start, elapsedTime return the number of seconds from init.
    */

    private final long start;

    public Stopwatch()
    {
        start = System.currentTimeMillis();
    }

    public double elapsedTime()
    {
        long now = System.currentTimeMillis();
        return (now - start) / 1000.0;
    }

    public static void main(String[] args)
    {
        Stopwatch timer = new Stopwatch();
        try{
            Thread.sleep(3000);
            double time = timer.elapsedTime();
            StdOut.println(time + "seconds pass");
        }
        catch(Exception e){}

    }
}