import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;

public class LinearProbingHashST<Key, Value>
{
    private static final int INIT_CAPACITY = 4;
    private int n;
    private int m;
    private Key[] keys;
    private Value[] values;

    public LinearProbingHashST(){
        this(INIT_CAPACITY);
    }

    public LinearProbingHashST(int capacity){
        m = capacity;
        n = 0;
        keys = (Key[]) new Object[m];
        values = (Value[]) new Object[m];
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

    private int hash(Key key){
        return (key.hashCode() & 0xfffffff) % m;
    }

    private void resize(int capacity){
        LinearProbingHashST<Key, Value> temp = new LinearProbingHashST<Key, Value>(capacity);
        for (int i = 0; i < m; i++) {
            if(keys[i] != null){
                temp.put(keys[i], values[i]);
            }
        }
        keys = temp.keys;
        values = temp.values;
        m = temp.m;
    }

    public void put(Key key, Value value){
        if (key == null) throw new IllegalArgumentException("first argsument to put() is null");
        if (value == null){
            delete(key);
            return;
        }

        if (n >= m/2) resize(2*m);

        int i = hash(key);
        for (; keys[i] != null; i = (i + 1) % m) {
            if(keys[i].equals(key)){
                values[i] = value;
                return;
            }
        }
        keys[i] = key;
        values[i] = value;
        n++;
    }

    public Value get(Key key){
        if (key == null) throw new IllegalArgumentException("argsument to get() is null");
        for (int i = hash(key); keys[i] != null; i = (i + 1) % m) {
            if (keys[i].equals(key))
                return values[i];
        }
        return null;
    }

    public void delete(Key key){
        if (key == null) throw new IllegalArgumentException("argsument to delete() is null");
        if (!contains(key)) return;

        int i = hash(key);
        while(!key.equals(keys[i]))
            i = (i + 1) % m;

        keys[i] = null;
        values[i] = null;

        i = (i + 1) % m;
        while(keys[i] != null){
            Key keyToRehash = keys[i];
            Value valueToRehash = values[i];
            keys[i] = null;
            values[i] = null;
            n--;
            put(keyToRehash, valueToRehash);
            i = (i + 1) % m;
        }
        n--;

        if (n > 0 && n <= m/8) resize(m/2);
    }

    public Iterable<Key> keys(){
        Queue<Key> queue = new Queue<Key>();
        for (int i = 0; i < m; i++) {
            if (keys[i] != null) queue.enqueue(keys[i]);
        }
        return queue;
    }

    public static void main(String[] args) {
        LinearProbingHashST<String,Integer> st = new LinearProbingHashST<String, Integer>();
        for (int i = 0; !StdIn.isEmpty(); i++) {
            String key = StdIn.readString();
            st.put(key, i);
        }

        for (String s : st.keys()) {
            StdOut.println(s + " " + st.get(s));
        }
    }
}

