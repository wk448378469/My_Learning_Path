import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdRandom;

public class FlowNetwork
{
    private static final String NEWLINE = System.getProperty("line.separator");
    private final int V;
    private int E;
    private Bag<FlowEdge>[] adj;

    public FlowNetwork(int V){
        if (V < 0) throw new IllegalArgumentException();

        this.V = V;
        this.E = 0;
        adj = (Bag<FlowEdge>[]) new Bag[V];
        for (int v = 0; v < V; v++) {
            adj[v] = new Bag<FlowEdge>();
        }
    }

    public FlowNetwork(int V, int E){
        this(V);

        if (E < 0) throw new IllegalArgumentException();
        for (int i = 0; i < E; i++) {
            int v = StdRandom.uniform(V);
            int w = StdRandom.uniform(V);
            double capacity = StdRandom.uniform(100);
            addEdge(new FlowEdge(v, w, capacity));
        }
    }

    public FlowNetwork(In in){
        this(in.readInt());

        int E = in.readInt();
        if (E < 0) throw new IllegalArgumentException();
        for (int i = 0; i < E; i++) {
            int v = in.readInt();
            int w = in.readInt();
            validateVertex(v);
            validateVertex(w);
            double capacity = in.readDouble();
            addEdge(new FlowEdge(v, w, capacity));
        }
    }

    public int V(){
        return V;
    }

    public int E(){
        return E;
    }

    private void validateVertex(int v){
        if (v < 0 || v >= V)
            throw new IllegalArgumentException();
    }

    public void addEdge(FlowEdge e){
        int v = e.from();
        int w = e.to();
        validateVertex(v); validateVertex(w);
        adj[v].add(e);
        adj[w].add(e);
        E++;
    }

    public Iterable<FlowEdge> adj(int v){
        validateVertex(v);
        return adj[v];
    }

    public Iterable<FlowEdge> edges(){
        Bag<FlowEdge> list = new Bag<FlowEdge>();
        for (int v = 0; v < V; v++) {
            for (FlowEdge e : adj(v)) {
                list.add(e);
            }
        }
        return list;
    }

    public String toString(){
        StringBuilder s = new StringBuilder();
        s.append(V + " " + E + NEWLINE);
        for (int v = 0; v < V; v++) {
            s.append(v + ":  ");
            for (FlowEdge e : adj(v)) {
                if (e.to() != v) s.append(e + "  ");
            }
            s.append(NEWLINE);
        }
        return s.toString();
    }

    public static void main(String[] args) {
        In in = new In(args[0]);
        FlowNetwork G = new FlowNetwork(in);
        StdOut.println(G);
    }
}
