import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;

public class SeparateChainingHashST<Key, Value>
{
    private static final int INIT_CAPACITY = 4;
    private int n;         //number of key-value pairs
    private int m;         //hash table size
    private SequentialSearchST<Key, Value>[] st;

    public SeparateChainingHashST(){
        this(INIT_CAPACITY);
    }

    public SeparateChainingHashST(int m){
        this.m = m;
        st = (SequentialSearchST<Key, Value>[]) new SequentialSearchST[m];
        for (int i = 0; i < m; i++) {
            st[i] = new SequentialSearchST<Key,Value>();
        }
    }

    private void resize(int chains){
        SeparateChainingHashST<Key, Value> temp = new SeparateChainingHashST<Key, Value>(chains);
        for (int i = 0; i < m; i++) {
            for (Key key : st[i].keys()) {
                temp.put(key, st[i].get(key));
            }
        }
        this.m = temp.m;
        this.n = temp.n;
        this.st = this.st;
    }

    private int hash(Key key){
        return (key.hashCode() & 0x7fffffff) % m;
    }

    public int size(){
        return n;
    }

    public boolean isEmpty(){
        return size() == 0;
    }

    public boolean contains(Key key){
        if (key == null) throw new IllegalArgumentException("argsument to contains() is null");
        return get(key) != null;
    }

    public Value get(Key key){
        if (key == null) throw new IllegalArgumentException("argsument to get() is null");
        int i = hash(key);
        return st[i].get(key);
    }

    public void put(Key key, Value value){
        if (key == null) throw new IllegalArgumentException("first argsument null");
        if (value == null) {
            delete(key);
            return;
        }

        if (n >= 10*m) resize(2*m);
        int i = hash(key);
        StdOut.println("key = " + key + " value = " + value + " hashcode = " + i + " current m = " + m);
        if (!st[i].contains(key)) n++;
        st[i].put(key, value);
    }

    public void delete(Key key){
        if (key == null) throw new IllegalArgumentException("argsument to delete() is null");
        int i = hash(key);
        if (st[i].contains(key)) n--;
        st[i].delete(key);

        if (m > INIT_CAPACITY && n <= 2*m) resize(m/2);
    }

    public Iterable<Key> keys(){
        Queue<Key> queue = new Queue<Key>();
        for (int i = 0; i < m; i++) {
            for (Key key : st[i].keys()) {
                queue.enqueue(key);
            }
        }
        return queue;
    }
    public static void main(String[] args) {
        SeparateChainingHashST<String, Integer> st = new SeparateChainingHashST<String, Integer>();
        for (int i = 0; !StdIn.isEmpty(); i++) {
            String key = StdIn.readString();
            st.put(key, i);
        }

        // print keys
        for (String s : st.keys()) 
            StdOut.println(s + " " + st.get(s)); 

    }
}