import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;

public class DeDup
{
    public static void main(String[] args) {
        SET<String> set = new SET<String>();
        while(!StdIn.isEmpty()){
            String key = StdIn.readString();
            if(!set.contains(key)){
                set.add(key);
                StdOut.println(key);
            }
        }
    }
}