import edu.princeton.cs.algs4.StdOut;
import java.util.NoSuchElementException;

public class IndexMinPQ<Key extends Comparable<Key>>
{
    private int maxN;
    private int n;
    private int[] pq;
    private int[] qp;
    private Key[] keys;

    public IndexMinPQ(int maxN)
    {
        if (maxN < 0) throw new IllegalArgumentException();
        this.maxN = maxN;
        n = 0;
        keys = (Key[]) new Comparable[maxN + 1];
        pq = new int[maxN + 1];
        qp = new int[maxN + 1];
        for(int i = 0; i <= maxN; i++)
            qp[i] = -1;
    }

    public void insert(int k, Key key)
    {
        if(k < 0 || k >= maxN) throw new IllegalArgumentException();
        if(contains(k)) throw new IllegalArgumentException("index is already in the priority queue");
        n++;
        qp[k] = n;
        pq[n] = k;
        keys[k] = key;
        swim(n);
    }

    public void change(int k, Key key)
    {
        if (k < 0 || k >= maxN) throw new IllegalArgumentException();
        if (!contains(k)) throw new NoSuchElementException("index is not in the priority queue");
        keys[k] = key;
        swim(qp[k]);
        sink(qp[k]);
    }

    public boolean contains(int k)
    {
        if ( k < 0 || k >= maxN) throw new IllegalArgumentException();
        return qp[k] != -1;
    }

    public void decreaseKey(int i, Key key){
        if (i < 0 || i >= maxN) throw new IllegalArgumentException();
        if (! contains(i)) throw new NoSuchElementException();
        if (keys[i].compareTo(key) <= 0)
            throw new IllegalArgumentException();
        keys[i] = key;
        swim(qp[i]);
    }

    public void increaseKey(int i, Key key){
        if (i < 0 || i >= maxN) throw new IllegalArgumentException();
        if (! contains(i)) throw new NoSuchElementException();
        if (keys[i].compareTo(key) <= 0)
            throw new IllegalArgumentException();
        keys[i] = key;
        sink(qp[i]);
    }

    public void delete(int k)
    {
        if (k < 0 || k >= maxN) throw new IllegalArgumentException();
        if (!contains(k)) throw new NoSuchElementException("index is not in the priority queue");
        int index = qp[k];
        exch(index, n--);
        swim(index);
        sink(index);
        keys[k] = null;
        qp[k] = -1;
    }

    public Key min()
    {
        if (n == 0) throw new NoSuchElementException("priority queue underflow");
        return keys[pq[1]];
    }

    public int minIndex()
    {
        if (n == 0) throw new NoSuchElementException("priority queue underflow");
        return pq[1];
    }

    public int delMin()
    {
        if (n == 0) throw new NoSuchElementException("priority queue underflow");
        int min = pq[1];
        exch(1, n--);
        sink(1);
        qp[min] = -1;
        keys[min] = null;
        pq[n+1] = -1;
        return min;
    }

    public boolean isEmpty()
    {
        return n == 0;
    }

    public int size()
    {
        return n;
    }

    private boolean greater(int i, int j)
    {
        return keys[pq[i]].compareTo(keys[pq[j]]) > 0;
    }

    private void exch(int i, int j)
    {
        int swap = pq[i];
        pq[i] = pq[j];
        pq[j] = swap;
        qp[pq[i]] = i;
        qp[pq[j]] = j;
    }

    private void swim(int k)
    {
        while (k > 1 && greater(k/2, k)) 
        {
            exch(k, k/2);
            k = k/2;
        }
    }

    private void sink(int k)
    {
        while (2*k <= n) 
        {
            int j = 2 * k;
            if (j < n && greater(j, j+1)) j++;
            if (!greater(k,j)) break;
            exch(k, j);
            k = j;
        }
    }

    public static void main(String[] args) 
    {
        String[] strings = { "it", "was", "the", "best", "of", "times", "it", "was", "the", "worst" };
        IndexMinPQ<String> pq = new IndexMinPQ<String>(strings.length);
        for (int i=0; i< strings.length; i++) 
            pq.insert(i, strings[i]);

        StdOut.println("size is : " + pq.size());

        while(!pq.isEmpty())
        {
            int i = pq.delMin();
            StdOut.println(i + " " + strings[i]);
        }
        StdOut.println();
    }
}