import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.In;

public class LookupCSV
{

    // java-algs4 LookupCSV algs4-data\ip.csv 0 1

    private LookupCSV(){}

    public static void main(String[] args) {
        int keyField = Integer.parseInt(args[1]);
        int valField = Integer.parseInt(args[2]);

        ST<String, String> st = new ST<String, String>();
        In in = new In(args[0]);
        while(in.hasNextLine()){
            String line = in.readLine();
            String[] tokens = line.split(",");
            String key = tokens[keyField];
            String value = tokens[valField];
            st.put(key, value);
        }

        StdOut.println("symbol table size = " + st.size());

        while(!StdIn.isEmpty()){
            String s = StdIn.readString();
            if (st.contains(s)) StdOut.println(st.get(s));
            else                StdOut.println("Not found");
        }
    }
}