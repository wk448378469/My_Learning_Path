import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class EdgeWeightedDirectedCycle
{
    private boolean[] marked;
    private DirectedEdge[] edgeTo;
    private boolean[] onStack;
    private Stack<DirectedEdge> cycle;

    public EdgeWeightedDirectedCycle(EdgeWeightedDigraph G){
        marked = new boolean[G.V()];
        onStack = new boolean[G.V()];
        edgeTo = new DirectedEdge[G.V()];
        for (int v = 0; v < G.V(); v++) {
            if(!marked[v]) dfs(G, v);
        }
    }

    private void dfs(EdgeWeightedDigraph G, int v){
        onStack[v] = true;
        marked[v] = true;
        for (DirectedEdge e : G.adj(v)) {
            int w = e.to();

            if (cycle != null) return;
            else if (!marked[w]){
                edgeTo[w] = e;
                dfs(G, w);
            }
            else if (onStack[w]){
                cycle = new Stack<DirectedEdge>();
                DirectedEdge f = e;
                while(f.from() != w){
                    cycle.push(f);
                    f = edgeTo[f.from()];
                }
                cycle.push(f);
                return;
            }
        }
        onStack[v] = false;
    }

    public boolean hasCycle(){
        return cycle != null;
    }

    public Iterable<DirectedEdge> cycle(){
        return cycle;
    }

    public static void main(String[] args) {
        int V = Integer.parseInt(args[0]);
        int E = Integer.parseInt(args[1]);
        int F = Integer.parseInt(args[2]);

        EdgeWeightedDigraph G = new EdgeWeightedDigraph(V);
        int [] vertices = new int[V];
        for (int i = 0; i < E; i++) {
            int v, w;
            do{
                v = StdRandom.uniform(V);
                w = StdRandom.uniform(V);
            }while(v >= w);

            double weight = StdRandom.uniform();
            G.addEdge(new DirectedEdge(v, w, weight));
        }

        for (int i = 0; i < F; i++) {
            int v = StdRandom.uniform(V);
            int w = StdRandom.uniform(V);
            double weight = StdRandom.uniform(0.0, 1.0);
            G.addEdge(new DirectedEdge(v, w, weight));
        }
        StdOut.println(G);

        EdgeWeightedDirectedCycle finder = new EdgeWeightedDirectedCycle(G);
        if (finder.hasCycle()){
            StdOut.print("Cycle: ");
            for (DirectedEdge e : finder.cycle()) {
                StdOut.print(e + "  ");
            }
            StdOut.println();
        }
        else{
            StdOut.println("No directed cycle~");
        }
    }
}