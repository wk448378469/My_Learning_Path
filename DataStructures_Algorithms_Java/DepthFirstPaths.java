import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;

public class DepthFirstPaths
{
    private boolean[] marked;        // marked[v] = is there an s-v path?
    private int[] edgeTo;            // edgeTo[v] = last edge on s-v path
    private final int s;             // source vertex

    public DepthFirstPaths(Graph G, int s){
        this.s = s;
        edgeTo = new int[G.V()];
        marked = new boolean[G.V()];
        validateVertex(s);
        dfs(G, s);
    }

    private void dfs(Graph G, int v){
        marked[v] = true;
        for (int w : G.adj(v)) {
            if (!marked[w]) {
                edgeTo[w] = v;
                dfs(G, w);
            }
        }
    }

    public boolean hasPathTo(int v){
        validateVertex(v);
        return marked[v];
    }

    public Iterable<Integer> pathTo(int v){
        validateVertex(v);
        if (!hasPathTo(v)) return null;
        Stack<Integer> path = new Stack<Integer>();
        for (int x = v; x != s; x = edgeTo[x]) {
            path.push(x);
        }
        path.push(s);
        return path;
    }

    private void validateVertex(int v){
        int V = marked.length;
        if (v < 0 || v >= V)
            throw new IllegalArgumentException(" v not in 0 - " + V);
    }

    public static void main(String[] args) {
        In in = new In(args[0]);
        Graph G = new Graph(in);
        int s = Integer.parseInt(args[1]);
        DepthFirstPaths dfs = new DepthFirstPaths(G, s);

        for (int v = 0; v < G.V(); v++) {
            if (dfs.hasPathTo(v)){
                StdOut.printf("%d to %d: ", s, v);
                for (int x : dfs.pathTo(v)) {
                    if (x == s) StdOut.print(x);
                    else        StdOut.print("-" + x);
                }
                StdOut.println();
            }
            else
            {
                StdOut.printf("%d to %d: not connected ", s, v);
                StdOut.println();
            }
        }
    }

}