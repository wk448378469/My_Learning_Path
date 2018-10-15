import edu.princeton.cs.algs4.StdOut;

public class TestBST
{
    public static void main(String[] args) {
        BST<String, Integer> bst = new BST<String, Integer>();
        String test = "E S H I J H G U Y Z O U A H S H K L Q U N B";
        String[] keys = test.split(" ");
        int n = keys.length;

        for (int i = 0; i < n; i++) {
            bst.put(keys[i], i);
        }

        StdOut.println("size = " + bst.size());
        StdOut.println("min key = " + bst.min_use_loop() + " value = " + bst.get(bst.min_use_loop()));
        StdOut.println("max key = " + bst.max() + " value = " + bst.get(bst.max()));
        StdOut.println();
        StdOut.println("--------------------------------");
        for (String s : bst.keys()) {
            StdOut.println(s + " " + bst.get(s));
        }
        StdOut.println("--------------------------------");
        StdOut.println();
        StdOut.println("Testing select");
        for (int i = 0; i < bst.size(); i++) {
            StdOut.println(i + " " + bst.select(i));
        }
        StdOut.println();
        StdOut.println("key rank floor ceil");
        StdOut.println("-------------------");
        for (char i = 'A'; i <= 'Z'; i++) {
            String s = i + "";
            StdOut.printf("%2s %4d %4s %4s\n", s, bst.rank(s), bst.floor(s), bst.ceiling(s));
        }
        StdOut.println();

        String[] from = { "A", "Z", "X", "0", "B", "C" };
        String[] to   = { "Z", "A", "X", "Z", "G", "L" };
        StdOut.println("range search");
        StdOut.println("-------------------");
        for (int i = 0; i < from.length; i++) {
            StdOut.printf("%s-%s : ", from[i], to[i]);
            for (String s : bst.keys(from[i], to[i]))
                StdOut.print(s + " ");
            StdOut.println();
        }
        StdOut.println();

        for (int i = 0; i < bst.size() / 2; i++) {
            bst.deleteMin();
        }
        StdOut.println("After deleting the smallest " + bst.size() / 2 + " keys");
        StdOut.println("--------------------------------");
        for (String s : bst.keys()) 
            StdOut.println(s + " " + bst.get(s)); 
        StdOut.println();
    }
}