import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;

public class Topological
{
    private Iterable<Integer> order;
    private int[] rank;

    public Topological(Digraph G){
        DirectedCycle finder = new DirectedCycle(G);
        if (!finder.hasCycle()) {
            DepthFirstOrder dfs = new DepthFirstOrder(G);
            order = dfs.reversePost();
            rank = new int[G.V()];
            int i = 0;
            for (int v : order) {
                rank[v] = i++;
            }
        }
    }

    public Topological(EdgeWeightedDigraph G){
        EdgeWeightedDirectedCycle finder = new EdgeWeightedDirectedCycle(G);
        if (!finder.hasCycle()){
            DepthFirstOrder dfs = new DepthFirstOrder(G);
            order = dfs.reversePost();
        }
    }

    public Iterable<Integer> order(){
        return order;
    }

    public boolean hasOrder(){
        return order != null;
    }

    public int rank(int v){
        validateVertex(v);
        if (hasOrder()) return rank[v];
        else            return -1;
    }

    private void validateVertex(int v){
        int V = rank.length;
        if (v < 0 || v >= V) {
            throw new IllegalArgumentException("bad v");
        }
    }

    public static void main(String[] args) {
        String filename = args[0];
        String delemiter = args[1];
        SymbolDigraph sg = new SymbolDigraph(filename, delemiter);
        Topological topological = new Topological(sg.digraph());
        for (int v : topological.order()) {
            StdOut.println(sg.nameOf(v));
        }
    }
}