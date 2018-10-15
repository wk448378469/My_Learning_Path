import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;

public class Digraph
{
    private static final String NEWLINE = System.getProperty("line.separator");

    private final int V;               // number of vertices
    private int E;                     // number of edges
    private Bag<Integer>[] adj;
    private int[] indegree;            // indegree[v] == indegree of vertex v

    public Digraph(int V){
        if (V < 0) throw new IllegalArgumentException("V need > 0");
        this.V = V;
        this.E = 0;
        indegree = new int[V];
        adj = (Bag<Integer>[]) new Bag[V];
        for (int v = 0; v < V; v++)
            adj[v] = new Bag<Integer>();
    }

    public Digraph(In in){
        try{
            this.V = in.readInt();
            if (V < 0) throw new IllegalArgumentException("bad number");
            indegree = new int[V];
            adj = (Bag<Integer>[]) new Bag[V];
            for (int v = 0; v < V; v++) {
                adj[v] = new Bag<Integer>();
            }

            int E = in.readInt();
            if (E < 0) throw new IllegalArgumentException("bad number");
            for (int i = 0; i < E; i++) {
                int v = in.readInt();
                int w = in.readInt();
                addEdge(v, w);
            }
        }
        catch (NoSuchElementException e){
            throw new IllegalArgumentException("invalid input format in digraph constructor", e);
        }
    }

    public Digraph(Digraph G){
        this(G.V());
        this.E = G.E();
        for (int v = 0; v < V; v++) {
            this.indegree[v] = G.indegree(v);
        }

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

    public int V(){
        return V;
    }

    public int E(){
        return E;
    }

    private void validateVertex(int v){
        if (v < 0 || v >= V) {
            throw new IllegalArgumentException("bad v");
        }
    }

    public void addEdge(int v, int w){
        validateVertex(v);
        validateVertex(w);
        adj[v].add(w);
        indegree[w]++;
        E++;
    }

    public Iterable<Integer> adj(int v){
        validateVertex(v);
        return adj[v];
    }

    public int outdegree(int v){
        validateVertex(v);
        return adj[v].size();
    }

    public int indegree(int v){
        validateVertex(v);
        return indegree[v];
    }

    public Digraph reverse(){
        Digraph reverse = new Digraph(V);
        for (int v = 0; v < V; v++) {
            for (int w : adj[v]) {
                reverse.addEdge(w, v);
            }
        }
        return reverse;
    }

    public String toString(){
        StringBuilder s = new StringBuilder();
        s.append(V + " vertices, " + E + " edges " + NEWLINE);
        for (int v = 0; v < V; v++) {
            s.append(String.format("%d: ", v));
            for (int w : adj[v]) {
                s.append(String.format("%d ", w));
            }
            s.append(NEWLINE);
        }
        return s.toString();
    }

    public static void main(String[] args) {
        In in = new In(args[0]);
        Digraph G = new Digraph(in);
        StdOut.println(G);
    }
}