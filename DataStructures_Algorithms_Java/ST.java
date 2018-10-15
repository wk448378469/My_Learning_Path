import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.TreeMap;

public class ST<Key extends Comparable<Key>, Value> implements Iterable<Key>
{

    private TreeMap<Key, Value> st;

    public ST(){
        st = new TreeMap<Key, Value>();
    }

    public void put(Key key, Value value){
        if(key == null) throw new IllegalArgumentException("null key");
        if(value == null) st.remove(key);
        else              st.put(key, value);
    }

    public Value get(Key key){
        if(key == null) throw new IllegalArgumentException("null key");
        return st.get(key);
    }

    public void delete(Key key){
        if(key == null) throw new IllegalArgumentException("null key");
        st.remove(key);
    }

    public boolean contains(Key key){
        if(key == null) throw new IllegalArgumentException("null key");
        return st.containsKey(key);
    }

    public boolean isEmpty(){
        return size() == 0;
    }

    public int size(){
        return st.size();
    }

    public Iterable<Key> keys(){
        return st.keySet();
    }

    @Deprecated
    public Iterator<Key> iterator() {
        return st.keySet().iterator();
    }

    public Key min(){
        if(isEmpty()) throw new NoSuchElementException("is empty");
        return st.firstKey();
    }

    public Key max(){
        if(isEmpty()) throw new NoSuchElementException("is empty");
        return st.lastKey();
    }

    public Key ceiling(Key key) {
        if (key == null) throw new IllegalArgumentException("argument to ceiling() is null");
        Key k = st.ceilingKey(key);
        if (k == null) throw new NoSuchElementException("all keys are less than " + key);
        return k;
    }

    public Key floor(Key key) {
        if (key == null) throw new IllegalArgumentException("argument to floor() is null");
        Key k = st.floorKey(key);
        if (k == null) throw new NoSuchElementException("all keys are greater than " + key);
        return k;
    }

}