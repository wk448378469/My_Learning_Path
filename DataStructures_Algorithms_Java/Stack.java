import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import java.util.Iterator;

public class Stack<Item> implements Iterable<Item>
{
    private Node<Item> first = null;  //the last node added in link
    private int N;

    private static class Node<Item>
    {
        Item item;
        Node<Item> next;
    }

    public boolean isEmpty()
    {
        return first == null;
    }

    public void push(Item item)
    {
        Node<Item> oldfirst = first;  // copy the last node
        first = new Node<Item>();     // define a new node 
        first.item = item;      // new node add attributes
        first.next = oldfirst;  // new node link the last node
        N++;
    }

    public Item pop()
    {
        Item item = first.item; // get the last node attributes
        first = first.next;       // last node pointer pointing last node next(parent node)
        N--;
        return item;
    }


    public int size()
    {
        return N;
    }

    public Iterator<Item> iterator()
    {
        return new ListIterator<Item>(first);
    }

    private class ListIterator<Item> implements Iterator<Item>
    {
        private Node<Item> current;

        public ListIterator(Node<Item> first)
        {
            current = first;
        }

        public boolean hasNext()
        {
            return current != null;
        }

        public void remove() { /*not supported!! */}

        public Item next()
        {
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    public static void main(String[] args) 
    {
        Stack<String> stack = new Stack<String>();
        while ( !StdIn.isEmpty())
        {
            String s = StdIn.readString();
            if (s.equals("-")) { StdOut.print(stack.pop() + " ");}
            else               { stack.push(s);}
        }
        StdOut.print("\nstack size is :" + stack.size() + "\n");

        for(String s : stack)
        {
            StdOut.println(s);
        }
    }
}