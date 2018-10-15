import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class LinkedStackOfStrings
{
    private Node first = null;  //the last node added in link

    private class Node
    {
        String item;
        Node next;
    }

    public boolean isEmpty()
    {
        return first == null;
    }

    public void push(String item)
    {
        Node oldfirst = first;  // copy the last node
        first = new Node();     // define a new node 
        first.item = item;      // new node add attributes
        first.next = oldfirst;  // new node link the last node
    }

    public String pop()
    {
        String item = first.item; // get the last node attributes
        first = first.next;       // last node pointer pointing last node next(parent node)
        return item;
    }


    public int size()
    {
        int size = 0;
        Node x = first;
        while (x.next != null)
        {
            x = x.next;
            size++;
        }
        size++;         // last node pointer is null, but is a node
        return size;
    }

    public static void main(String[] args) 
    {
        LinkedStackOfStrings stack = new LinkedStackOfStrings();
        while ( !StdIn.isEmpty())
        {
            String s = StdIn.readString();
            if (s.equals("-")) { StdOut.print(stack.pop() + " ");}
            else               { stack.push(s);}
        }
        StdOut.print("\nstack size is :" + stack.size());
    }
}