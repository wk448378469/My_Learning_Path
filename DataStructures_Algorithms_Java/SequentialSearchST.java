import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class SequentialSearchST<Key, Value>
{
    private int n;  // number of pair
    private Node first;

    private class Node{
        private Key key;
        private Value value;
        private Node next;

        public Node(Key key, Value value, Node next){
            this.key = key;
            this.value = value;
            this.next = next;
        }
    }


    public int size(){
        return n;
    }

    public boolean isEmpty(){
        return n == 0;
    }

    public boolean contains(Key key){
        if(key == null) throw new IllegalArgumentException("key is null");
        return get(key) != null;
    }

    public Value get(Key key){
        if(key == null) throw new IllegalArgumentException("key is null");
        for (Node x = first; x != null;  x = x.next) {
            if(key.equals(x.key))
                return x.value;
        }
        return null;
    }

    public void put(Key key, Value value){
        if(key == null) throw new IllegalArgumentException("key is null");
        if(value == null) {
            delete(key);
            return;
        }

        for (Node x = first; x != null;  x = x.next) {
            if(key.equals(x.key)){
                x.value = value;
                return;
            }
        }
        first = new Node(key, value, first);
        n++;
    }

    public void delete(Key key){
        if(key == null) throw new IllegalArgumentException("key is null");
        first = delete(first, key);
    }

    private Node delete(Node x, Key key){
        if(x == null) return null;
        if(key.equals(x.key)){
            n--;
            return x.next;
        }
        x.next = delete(x.next, key);
        return x;
    }

    public Iterable<Key> keys(){
        Queue<Key> queue = new Queue<Key>();
        for (Node x = first; x != null; x = x.next)
            queue.enqueue(x.key);
        return queue;
    }

    public static void main(String[] args) { 
        SequentialSearchST<String, Integer> st = new SequentialSearchST<String, Integer>();
        for (int i = 0; !StdIn.isEmpty(); i++) {
            String key = StdIn.readString();
            st.put(key, i);
        }
        for (String s : st.keys())
            StdOut.println(s + " " + st.get(s));
    }
}