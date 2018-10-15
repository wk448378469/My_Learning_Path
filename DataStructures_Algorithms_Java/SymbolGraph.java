import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.In;

public class SymbolGraph
{
    private ST<String, Integer> st;
    private String[] keys;
    private Graph graph;

    public SymbolGraph(String filename, String delimiter){
        st = new ST<String, Integer>();

        In in = new In(filename);
        while(!in.isEmpty()){
            String[] a = in.readLine().split(delimiter);
            for (int i = 0; i < a.length; i++) {
                if (!st.contains(a[i])) {
                    st.put(a[i], st.size());
                }
            }
        }

        keys = new String[st.size()];
        for (String name : st.keys()) {
            keys[st.get(name)] = name;
        }

        graph = new Graph(st.size());
        in = new In(filename);
        while(in.hasNextLine()){
            String[] a = in.readLine().split(delimiter);
            int v = st.get(a[0]);
            for (int i = 1;  i < a.length; i++) {
                int w = st.get(a[i]);
                graph.addEdge(v, w);
            }
        }
    }


    public boolean contains(String s){
        return st.contains(s);
    }

    public int indexOf(String s){
        return st.get(s);
    }

    public String nameOf(int v){
        validateVertex(v);
        return keys[v];
    }

    public Graph graph(){
        return graph;
    }

    private void validateVertex(int v){
        int V = graph.V();
        if (v < 0 || v >= V) {
            throw new IllegalArgumentException("v must in 0 - " + (V-1));
        }
    }

    public static void main(String[] args) {
        String filename = args[0];
        String delimiter = args[1];
        SymbolGraph sg = new SymbolGraph(filename, delimiter);
        Graph graph = sg.graph();

        while(StdIn.hasNextLine()){
            String source = StdIn.readLine();
            if (sg.contains(source)){
                int s = sg.indexOf(source);
                for (int v : graph.adj(s)) {
                    StdOut.println("    " + sg.nameOf(v));
                }
            }
            else{
                StdOut.println("input not contain '" + source + "'");
            }
        }
    }
}