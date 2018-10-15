import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;

public class Graph
{
    private static final String NEWLINE = System.getProperty("line.separator");
    private final int V;
    private int E;
    private Bag<Integer>[] adj;

    public Graph(int V){
        if (V < 0) throw new IllegalArgumentException("need V >= 0");
        this.V = V;
        this.E = 0;
        adj = (Bag<Integer>[]) new Bag[V];
        for (int v = 0; v < V; v++) {
            adj[v] = new Bag<Integer>();
        }
    }

    public Graph(In in){
        try{
            this.V = in.readInt();
            if (V < 0) throw new IllegalArgumentException("need V >= 0");
            adj = (Bag<Integer>[]) new Bag[V];
            for (int v = 0; v < V ; v++) {
                adj[v] = new Bag<Integer>();
            }

            int E = in.readInt();
            if (E < 0) throw new IllegalArgumentException("need E >= 0");
            for (int i = 0; i <E; i++) {
                int v = in.readInt();
                int w = in.readInt();
                validateVertex(v);
                validateVertex(w);
                addEdge(v,w);
            }
        }
        catch(NoSuchElementException e){
            throw new IllegalArgumentException("invalid input format in graph constructor", e);
        }
    }

    public Graph(Graph G){
        this(G.V());
        this.E = G.E();
        for (int v = 0; v < G.V(); v++) {
            Stack<Integer> reverse = new Stack<Integer>();
            for (int w : G.adj(v)) {
                reverse.push(w);
            }

            for (int w : reverse) {
                adj[v].add(w);
            }
        }
    }

    public int E(){
        return E;
    }

    public int V(){
        return V;
    }

    private void validateVertex(int v){
        if (v < 0 || v >= V)
            throw new IllegalArgumentException(" v not in 0 - " + V);
    }

    public void  addEdge(int v, int w){
        validateVertex(v);
        validateVertex(w);
        E++;
        adj[v].add(w);
        adj[w].add(v);
    }

    public Iterable<Integer> adj(int v){
        validateVertex(v);
        return adj[v];
    }

    public boolean hasEdge(int v, int w){
        validateVertex(v);
        validateVertex(w);
        Bag<Integer> temp = adj[v];
        for (int x : temp) {
            if (x == w)
                return true;
        }
        return false;
    }

    public int degree(int v){
        validateVertex(v);
        return adj[v].size();
    }

    public String toString(){
        StringBuilder s = new StringBuilder();
        s.append(V + " vertices, " + E + " edges " + NEWLINE);
        for (int v = 0; v < V; v++) {
            s.append(v + ": ");
            for (int w : adj[v]) {
                s.append(w + " ");
            }
            s.append(NEWLINE);
        }
        return s.toString();
    }

    public static void main(String[] args) {
        In in = new In(args[0]);
        Graph G = new Graph(in);
        StdOut.println(G);

        StdOut.println("0 to 6 is direct connected ? " + G.hasEdge(0,6));
    }
}