import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.In;

public class BlackFilter
{

    // java-algs4 WhiteFilter algs4-data\list.txt < tinyTale.txt

    private BlackFilter(){}

    public static void main(String[] args) {
        SET<String> set = new SET<String>();

        In in = new In(args[0]);
        while(!in.isEmpty()){
            String word = in.readString();
            set.add(word);
        }
    
        while(!StdIn.isEmpty()){
            String word = StdIn.readString();
            if (!set.contains(word))
                StdOut.println(word);
        }
    }
}