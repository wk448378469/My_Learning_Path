import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;

public class LazyPrimMST
{
    private static final double FLOATING_POINT_EPSILON = 1E-12;
    private double weight;      // total weight
    private Queue<Edge> mst;
    private boolean[] marked;
    private MinPQ<Edge> pq;

    public LazyPrimMST(EdgeWeightedGraph G){
        mst = new Queue<Edge>();
        pq = new MinPQ<Edge>();
        marked = new boolean[G.V()];
        for (int v = 0; v < G.V(); v++) {
            if(!marked[v]) prim(G, v);
        }
    }

    private void prim(EdgeWeightedGraph G, int s){
        scan(G, s);
        while(!pq.isEmpty()){
            Edge e = pq.delMin();
            int v = e.either();
            int w = e.other(v);
            assert marked[v] || marked[w];
            if (marked[v] && marked[w]) continue;

            mst.enqueue(e);
            weight += e.weight();
            if (!marked[v]) scan(G, v);
            if (!marked[w]) scan(G, w);
        }
    }

    private void scan(EdgeWeightedGraph G, int v){
        assert !marked[v];
        marked[v] = true;
        for (Edge e : G.adj(v)) {
            if (!marked[e.other(v)]) pq.insert(e);
        }
    }

    public Iterable<Edge> edges(){
        return mst;
    }

    public double weight(){
        return weight;
    }

    public static void main(String[] args) {
        In in = new In(args[0]);
        EdgeWeightedGraph G = new EdgeWeightedGraph(in);
        LazyPrimMST mst = new LazyPrimMST(G);
        for (Edge e : mst.edges()) {
            StdOut.println(e);
        }
        StdOut.printf("%.5f\n", mst.weight());
    }

}