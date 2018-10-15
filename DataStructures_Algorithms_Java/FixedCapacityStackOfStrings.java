import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class FixedCapacityStackOfStrings{

    private String[] s;
    private int N;

    public FixedCapacityStackOfStrings(int capacity)
    {
        s = new String[capacity];
    }

    public boolean isEmpty()
    {
        return N == 0;
    }

    public void push(String item)
    {
        s[N++] = item;
    }

    public String pop()
    {
        String item = s[--N];
        s[N] = null;
        return item;
    }

    public int size()
    {
        int size = 0;
        for (int i = 0; i < s.length; i++)
        {
            if (s[i] != null) {size++;}
            else              {break;}
        }
        return size;
    }

    public static void main(String[] args) 
    {
        FixedCapacityStackOfStrings stack = new FixedCapacityStackOfStrings(20);
        while ( !StdIn.isEmpty())
        {
            String s = StdIn.readString();
            if (s.equals("-")) { StdOut.print(stack.pop() + " ");}
            else               { stack.push(s);}
        }
        StdOut.print("\nstack size is :" + stack.size());
    }

}