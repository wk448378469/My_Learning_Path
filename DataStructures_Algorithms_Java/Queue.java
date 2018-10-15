import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import java.util.Iterator;

public class Queue<Item> implements Iterable<Item>
{
    private Node<Item> first = null;
    private Node<Item> last = null;
    private int n = 0;

    private static class Node<Item>
    {
        Item item;
        Node<Item> next;
    }

    public boolean isEmpty()
    {
        return first == null;
    }

    public void enqueue(Item item)
    {
        Node<Item> oldlast = last;
        last = new Node<Item>();
        last.item = item;
        last.next = null;
        if (isEmpty()) { first = last;}
        else           { oldlast.next = last;}
        n++;
    }

    public int size(){
        return n;
    }

    public Item dequeue()
    {
        Item item = first.item;
        first = first.next;
        if( isEmpty()) { last = null;}
        n--;
        return item;
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

        public void remove(){ /*not supported!! */}

        public Item next()
        {
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    public static void main(String[] args) 
    {
        Queue<String> queue = new Queue<String>();

        while ( !StdIn.isEmpty())
        {
            String s = StdIn.readString();
            if (s.equals("-")) { StdOut.print(queue.dequeue() + " ");}
            else               { queue.enqueue(s);}
        }

        for(String q : queue)
        {
            StdOut.println(q);
        }
    }

}