import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import java.util.Iterator;

public class RandomizedQueue<Item> implements Iterable<Item> 
{
    private Item[] arrays;
    private int N;
    private int count;

    public RandomizedQueue()
    {
        // construct an empty randomized queue
        arrays = (Item[]) new Object[1];
        count = 0;
    }

    private void resize(int capacity)
    {
        Item[] copy = (Item[]) new Object[capacity];
        for(int i = 0; i < count; i++)
        {
            copy[i] = arrays[i];
        }
        arrays = copy;
    }

    public boolean isEmpty()
    {
        // is the randomized queue empty?
        return count == 0;
    }

    public int size()
    {
        // return the number of items on the randomized queue
        return count;
    }

    public void enqueue(Item item)
    {
        // add the item
        if (item == null) throw new java.lang.NullPointerException();
        if ( N == arrays.length) resize( 2*arrays.length);
        arrays[N++] = item;
        count++;
    }

    public Item dequeue()
    {
        // remove and return a random item
        if (isEmpty()) throw new java.util.NoSuchElementException();
        int index = StdRandom.uniform(N);
        Item item = arrays[index];

        arrays[index] = arrays[--N];
        arrays[N] = null;
        count--;

        if( count > 0 && count == arrays.length / 4) resize(arrays.length / 2);
        return item;
    }

    public Item sample()
    {
        if (isEmpty()) throw new java.util.NoSuchElementException();
        int index = StdRandom.uniform(N);
        Item item = arrays[index];
        return item;
    }

    public Iterator<Item> iterator()
    {
        // return an independent iterator over items in random order
        return new ArrayIterator();
    }


    private class ArrayIterator implements Iterator<Item>
    {
        private int i = 0;
        private Item[] copy;

        public ArrayIterator()
        {
            copy = (Item[]) new Object[count];
            for (int i = 0; i < count; i++) copy[i] = arrays[i];
            for (int j = 0; j < count; j++) 
            {
                int r = StdRandom.uniform(j+1);
                Item tmp = copy[j];
                copy[j] = copy[r];
                copy[r] = tmp;
            }
        }

        public boolean hasNext() { return i < count;}
        public void remove() { throw new java.lang.UnsupportedOperationException();}
        public Item next()
        {
            if (i >= count) throw new java.util.NoSuchElementException();
            return copy[i++];
        }
    }

    public static void main(String[] args)
    {
        // test
        RandomizedQueue<Integer> z = new RandomizedQueue<Integer>();
        z.enqueue(1);
        z.enqueue(4);
        z.enqueue(3);
        z.enqueue(6);
        z.enqueue(7);
        z.enqueue(8);
        z.enqueue(41);
        z.enqueue(53);
        StdOut.printf("size of queue: %d\n", z.size());

        for (int i : z) {
            StdOut.printf("outer i = %d\n", i);
            StdOut.println();
        }

        StdOut.printf("random dequeue i = " + z.dequeue() + "\n");
        StdOut.printf("random sample i = " + z.sample());
    }
}