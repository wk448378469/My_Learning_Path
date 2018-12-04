import java.util.*;

class Solution {
    private HashMap<String, ArrayList<String>> graph;
    private HashMap<String, ArrayList<Double>> weight;

    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {
        graph = new HashMap<String, ArrayList<String>>();
        weight = new HashMap<String, ArrayList<Double>>();

        for (int i = 0; i < equations.length; i++) {
            if (!graph.containsKey(equations[i][0])) {
                graph.put(equations[i][0], new ArrayList<String>());
                weight.put(equations[i][0], new ArrayList<Double>());
            }
            if (!graph.containsKey(equations[i][1])) {
                graph.put(equations[i][1], new ArrayList<String>());
                weight.put(equations[i][1], new ArrayList<Double>());
            }
            graph.get(equations[i][0]).add(equations[i][1]);
            graph.get(equations[i][1]).add(equations[i][0]);
            weight.get(equations[i][0]).add(values[i]);
            weight.get(equations[i][1]).add(1/values[i]);
        }

        double[] result = new double[queries.length];
        for (int i = 0; i < queries.length; i++) {
            result[i] = dfs(queries[i][0], queries[i][1], new HashSet<String>(), 1.0);
            if (result[i] == 0) result[i] = -1.0;
        }
        return result;
    }

    private double dfs(String molecule, String denominator, HashSet<String> marked, double value){
        if (marked.contains(molecule)) return 0.0;
        if (!graph.containsKey(molecule)) return 0.0;
        if (molecule.equals(denominator)) return value;

        marked.add(molecule);

        ArrayList<String> strList = graph.get(molecule);
        ArrayList<Double> valList = weight.get(molecule);
        double temp = 0.0;
        for (int i = 0; i < strList.size(); i++) {
            temp = dfs(strList.get(i), denominator, marked, value*valList.get(i));
            if (temp != 0.0) break;
        }

        marked.remove(molecule);
        return temp;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        String[][] e = {{"a", "b"}, {"b", "c"}};
        double[] v = {2.0, 3.0};
        String[][] q = {{"a", "c"}, {"b", "a"}, {"a", "e"}, {"a", "a"}, {"x", "x"}};
        double[] result = s.calcEquation(e, v, q);
        for (double r : result) {
            System.out.print(r + "  ");
        }
    }
}