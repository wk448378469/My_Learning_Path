import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;

public class KruskalMST
{
    private static final double FLOATING_POINT_EPSILON = 1E-12;
    private double weight;
    private Queue<Edge> mst = new Queue<Edge>();

    public KruskalMST(EdgeWeightedGraph G){
        MinPQ<Edge> pq = new MinPQ<Edge>();
        for (Edge e : G.edges()) {
            pq.insert(e);
        }

        UF uf = new UF(G.V());
        while(!pq.isEmpty() && mst.size() < G.V() - 1){
            Edge e = pq.delMin();
            int v = e.either();
            int w = e.other(v);
            if (!uf.connected(v, w)) {
                uf.union(v, w);
                mst.enqueue(e);
                weight += e.weight();
            }
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
        KruskalMST mst = new KruskalMST(G);
        for (Edge e : mst.edges()) {
            StdOut.println(e);
        }
        StdOut.printf("%.5f\n", mst.weight());
    }
}