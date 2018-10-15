import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;

public class TransitiveClosure
{
    private DirectedDFS[] tc;

    public TransitiveClosure(Digraph G){
        tc = new DirectedDFS[G.V()];
        for (int v = 0; v < G.V(); v++) {
            tc[v] = new DirectedDFS(G, v);
        }
    }

    public boolean reachable(int v, int w){
        validateVertex(v);
        validateVertex(w);
        return tc[v].marked(w);
    }

    private void validateVertex(int v){
        int V = tc.length;
        if (v < 0 || v >= V) {
            throw new IllegalArgumentException(" 0 <= v <V");
        }
    }

    public static void main(String[] args) {
        In in = new In(args[0]);
        Digraph G = new Digraph(in);

        TransitiveClosure tc = new TransitiveClosure(G);

        StdOut.print("      ");
        for (int v = 0; v < G.V(); v++) {
            StdOut.printf("%3d", v);
        }

        StdOut.println();
        StdOut.println("------------------------------------------");

        for (int v = 0; v < G.V(); v++) {
            StdOut.printf("%3d: ", v);
            for (int w = 0; w < G.V(); w++) {
                if (tc.reachable(v, w)) StdOut.printf("   T");
                else                    StdOut.printf("    ");
            }
            StdOut.println();
        }
    }
}