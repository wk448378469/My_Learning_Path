import edu.princeton.cs.algs4.StdOut;

public class DirectedEdge
{
    private final int v;
    private final int w;
    private final double weight;

    public DirectedEdge(int v, int w, double weight){
        if (v < 0) throw new IllegalArgumentException();
        if (w < 0) throw new IllegalArgumentException();
        if (Double.isNaN(weight)) throw new IllegalArgumentException();
        this.v = v;
        this.w = w;
        this.weight = weight;
    }

    public int from(){
        return v;
    }

    public int to(){
        return w;
    }

    public double weight(){
        return weight;
    }

    public String toString(){
        return v + "->" + w + " " + String.format("%5.2f", weight);
    }

    public static void main(String[] args) {
        DirectedEdge e = new DirectedEdge(23, 22, 52.2);
        StdOut.println(e);
    }
}