import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;

public class MaxPQ<Key extends Comparable<Key>>
{
    private Key[] pq;
    private int N = 0;

    public MaxPQ(int maxN)
    {
        pq = (Key[]) new Comparable[maxN + 1]; // pq[0] no used
    }

    public MaxPQ() {
        this(1);
    }

    public boolean isEmpty()
    {
        return N == 0;
    }

    public int size()
    {
        return N;
    }

    public void insert(Key v)
    {
        if (N == pq.length - 1) resize(2 * pq.length);

        pq[++N] = v;   // end insert
        swim(N);
    }

    public Key delMax()
    {
        Key max = pq[1];  // root node is max
        exch(1, N--);     // exchange the last
        pq[N+1] = null;   // preventing object dissociation

        if((N>0) && (N == (pq.length - 1)/4)) resize(pq.length / 2);

        sink(1);          // order
        return max;
    }

    public void resize(int capacity)
    {
        Key[] temp = (Key[]) new Comparable[capacity];
        for(int i = 1; i <= N; i++)
        {
            temp[i] = pq[i];
        }
        pq = temp;
    }

    private boolean less(int i, int j)
    {
        return pq[i].compareTo(pq[j]) < 0;
    }

    private void exch(int i, int j)
    {
        Key t = pq[i];
        pq[i] = pq[j];
        pq[j] = t;
    }

    private void swim(int k)
    {
        // down to up check current node is larger than parent node
        while(k > 1 && less(k/2, k))
        {
            exch(k/2, k);
            k = k/2;
        }
    }

    private void sink(int k)
    {
        // up to down check current node is smaller than child node
        while(2 * k <= N)
        {
            int j = 2 * k;
            if (j < N && less(j, j + 1)) j++;
            if (!less(k, j)) break;
            exch(k, j);
            k = j;
        }
    }

    public static void main(String[] args) 
    {
        MaxPQ<String> pq = new MaxPQ<String>();
        while (!StdIn.isEmpty()) {
            String item = StdIn.readString();
            if (!item.equals("-")) pq.insert(item);
            else if (!pq.isEmpty()) StdOut.print(pq.delMax() + " ");
        }
        StdOut.println("(" + pq.size() + " left on pq)");
    }
}