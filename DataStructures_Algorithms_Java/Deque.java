import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import java.util.Iterator;

public class Deque<Item> implements Iterable<Item> 
{
    private Node init;
    private int count;

    private class Node
    {
        Item item;
        Node next;
        Node prev;
    }

    public Deque()
    {
        init = new Node();
        init.item = null;
        init.next = init;
        init.prev = init;
        count = 0;
    }

    public boolean isEmpty()
    {
        return count == 0;
    }

    public int size()
    {
        return count;
    }

    public void addFirst(Item item)
    {
        if (item == null) throw new java.lang.NullPointerException("error");
        Node theOne = new Node();
        theOne.item = item;
        theOne.next = init.next;
        theOne.prev = init;

        init.next.prev = theOne;
        init.next = theOne;
        count++;

    }

    public void addLast(Item item)
    {
        if (item == null) throw new java.lang.NullPointerException("error");

        Node theOne = new Node();
        theOne.item = item;
        theOne.next = init;
        theOne.prev = init.prev;

        init.prev.next = theOne;
        init.prev = theOne;
        count++;
    }

    public Item removeFirst()
    {
        if( isEmpty()) throw new java.util.NoSuchElementException("error");

        Node theOne = init.next;
        Item theOneItem = theOne.item;

        init.next = theOne.next;
        theOne.next.prev = init;

        theOne = null;
        count--;
        return theOneItem;
    }

    public Item removeLast()
    {
        if( isEmpty()) throw new java.util.NoSuchElementException("error");

        Node theOne = init.prev;
        Item theOneItem = theOne.item;

        init.prev = theOne.prev;
        theOne.prev.next = init;

        theOne = null;
        count--;
        return theOneItem;
    }

    public Iterator<Item> iterator()
    {
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item>
    {
        private Node current;

        public ListIterator() { current = init.next;}

        public boolean hasNext() {return current != init;}

        public void remove() {throw new java.lang.UnsupportedOperationException();}

        public Item next()
        {
            if (current == init)
                throw new java.util.NoSuchElementException();
            Item item = current.item;
            current   = current.next;
            return item;
        }
    }

    public static void main(String[] args)
    {
        Deque<String> deque = new Deque<String>();
        while ( !StdIn.isEmpty())
        {
            String s = StdIn.readString();
            if (s.equals("-")) { StdOut.print(deque.removeFirst() + " ");}
            else               { deque.addFirst(s);}
        }
        StdOut.print("\nstack size is :" + deque.size() + "\n");

        for(String d : deque)
        {
            StdOut.println(d);
        }
    }
}