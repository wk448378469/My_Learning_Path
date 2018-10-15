import edu.princeton.cs.algs4.StdOut;

public class FordFulkerson
{
    private static final double FLOATING_POINT_EPSILON = 1E-11;
    private final int V;
    private boolean[] marked;
    private FlowEdge[] edgeTo;
    private double value;

    public FordFulkerson(FlowNetwork G, int s, int t){
        V = G.V();
        validate(s);
        validate(t);

        if (s == t)               throw new IllegalArgumentException();
        if (!isFeasible(G, s, t)) throw new IllegalArgumentException();

        value = excess(G, t);
        while(hasAugmentingPath(G, s, t)){
            double bottle = Double.POSITIVE_INFINITY;
            for (int v = t; v != s; v = edgeTo[v].other(v)) {
                bottle = Math.min(bottle, edgeTo[v].residualCapacityTo(v));
            }

            for (int v = t; v != s; v = edgeTo[v].other(v)) {
                edgeTo[v].addResidualFlowTo(v, bottle);
            }

            value += bottle;
        }
    }

    public double value(){
        return value;
    }

    public boolean inCut(int v){
        validate(v);
        return marked[v];
    }

    private void validate(int v){
        if (v < 0 || v >= V)
            throw new IllegalArgumentException();
    }

    private boolean hasAugmentingPath(FlowNetwork G, int s, int t){
        edgeTo = new FlowEdge[G.V()];
        marked = new boolean[G.V()];

        Queue<Integer> queue = new Queue<Integer>();
        queue.enqueue(s);
        marked[s] = true;
        while(!queue.isEmpty() && !marked[t]){
            int v = queue.dequeue();
            for (FlowEdge e : G.adj(v)) {
                int w = e.other(v);
                if (e.residualCapacityTo(w) > 0){
                    if (!marked[w]){
                        edgeTo[w] = e;
                        marked[w] = true;
                        queue.enqueue(w);
                    }
                }
            }
        }
        return marked[t];
    }

    private double excess(FlowNetwork G, int v){
        double excess = 0.0;
        for (FlowEdge e : G.adj(v)) {
            if (v == e.from()) excess -= e.flow();
            else               excess += e.flow();
        }
        return excess;
    }

    private boolean isFeasible(FlowNetwork G, int s, int t){
        for (int v = 0; v < G.V(); v++) {
            for (FlowEdge e : G.adj(v)) {
                if (e.flow() < -FLOATING_POINT_EPSILON || e.flow() > e.capacity() + FLOATING_POINT_EPSILON){
                    System.err.println("ha ~");
                    return false;
                }
            }
        }

        if (Math.abs(value + excess(G,s)) > FLOATING_POINT_EPSILON){
            System.err.println("hei~");
            return false;
        }

        if (Math.abs(value - excess(G,t)) > FLOATING_POINT_EPSILON){
            System.err.println("asd~");
            return false;
        }

        for (int v = 0; v < G.V(); v++) {
            if (v == s || v == t) continue;
            else if (Math.abs(excess(G,v)) > FLOATING_POINT_EPSILON){
                System.err.println("!@#");
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int V = Integer.parseInt(args[0]);
        int E = Integer.parseInt(args[1]);
        int s = 0, t = V - 1;
        FlowNetwork G = new FlowNetwork(V, E);
        StdOut.println(G);

        FordFulkerson maxflow = new FordFulkerson(G, s, t);
        StdOut.println("Max flow from " + s + " to " + t);
        for (int v = 0; v < G.V(); v++) {
            for (FlowEdge e : G.adj(v)) {
                if ((v == e.from()) && e.flow() > 0)
                    StdOut.println("    " + e);
            }
        }

        StdOut.print("Min cut: ");

        for (int v = 0; v < G.V(); v++) {
            if (maxflow.inCut(v)) StdOut.print(v + " ");
        }
        StdOut.println();

        StdOut.println("Max flow value = " + maxflow.value());
    }
}