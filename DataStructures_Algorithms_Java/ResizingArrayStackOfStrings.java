import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class ResizingArrayStackOfStrings{

    private String[] s;
    private int N;

    public ResizingArrayStackOfStrings()
    {
        s = new String[1];
    }

    public boolean isEmpty()
    {
        return N == 0;
    }

    public void push(String item)
    {
        if (N == s.length) {resize(2 * s.length);}
        s[N++] = item;
    }

    private void resize(int capacity)
    {
        String[] copy = new String[capacity];
        for (int i = 0; i < N; i++)
        {
            copy[i] = s[i];
        }
        s = copy;
    }

    public String pop()
    {
        String item = s[--N];
        s[N] = null;
        if (N > 0 && N == s.length / 4) { resize(s.length /2);}
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
        ResizingArrayStackOfStrings stack = new ResizingArrayStackOfStrings();
        while ( !StdIn.isEmpty())
        {
            String s = StdIn.readString();
            if (s.equals("-")) { StdOut.print(stack.pop() + " ");}
            else               { stack.push(s);}
        }
        StdOut.print("\nstack size is :" + stack.size());
    }

}