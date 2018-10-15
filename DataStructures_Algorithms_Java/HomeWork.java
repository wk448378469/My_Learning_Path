import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdRandom;
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

public class HomeWork{

    public static int lg(int N)
    {
        /* 
            home work 1.1.14
            args    : integer
            return  : maximum integer that is not bigger than log2N
        */
        int i = 0;
        int result = 0;      //  

        do
        {
            if (i == 0) { result = 0 ;}
            else 
            {
                result = 2;
                for (int j = 0 ; j <= i; j ++)
                {
                    result = result * 2;
                }
            }
            i = i + 1;
        }while(result <= N);

        return i;
    }

    public static int[] histogram(int[] a, int M)
    {
        /* 
            home work 1.1.15
            args    : a -- int[]
                      M -- int
            return  : histogram -- int[]
                      histogram's length is M, each value is number of occurrences of index in the args a.
        */
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < a.length; i++)
        {
            Integer nums = map.get(a[i]);
            if( nums != null) { map.put(a[i], nums + 1);}
            else              { map.put(a[i], 1);} 
        }

        int [] histogram = new int[M];
        for (int i = 0; i < histogram.length; i++)
        {
            Integer times = map.get(i);
            if (times == null) { histogram[i] = 0;}
            else               { histogram[i] = times;}
        }

        return histogram;
    }

    public static int mystery1(int a, int b)
    {
        /* 
            home work 1.1.18
            return  : a**b
        */
        if (b == 0)     return 1;
        if (b % 2 == 0) return mystery1(a*a, b/2);
        return mystery1(a*a, b/2) * a;
    }

    public static int mystery2(int a, int b)
    {
        /* 
            home work 1.1.18
            return  : a*b
        */
        if (b == 0)     return 0;
        if (b % 2 == 0) return mystery2(a+a, b/2);
        return mystery2(a+a, b/2) + a;
    }


    public static double recursion_ln(int N)
    {
        /* 
            home work 1.1.20
            return  : ln(N!)
        */
        if (N == 1) return 0;
        return recursion_ln(N - 1) + Math.log(N);
    }

    public static int euclid(int n, int m)
    {
        /* 
            home work 1.1.24
            return  : the maximum common divisor of m and n
        */
        int max;
        int min;
        if (n > m)          { max = n; min = m;}
        else if (n < m)     { max = m; min = n;}
        else return n;

        int p = max / min;
        int q = max % min;
        //StdOut.println(max + "=" + p + "*" + min + "+" + q);
        if (q == 0) {return min;}
        else return euclid(min, q);
    }


    public static double[] prob()
    {
        /* 
            return  : probability distribution of two dice sums as a array
        */
        int SIDES = 6;
        double[] dist = new double[2*SIDES + 1];
        for (int i = 1; i <= SIDES; i++)
        {
            for (int j = 1; j <= SIDES; j++)
            {
                dist[i+j] += 1.0;
            }
        }

        for (int k = 2; k <= 2*SIDES; k++)
        {
            dist[k] /= 36.0;
        }
        return dist;
    }

    public static void diceExperiment()
    {
        /* 
            home work 1.1.35
            return  : repeat N times to get two dice sum, and calc the probability
        */

        double[] prob = prob();   //standard probability
        int N = 1;              //number of experiment
        int[] experiment = new int[prob.length];

        while (true)
        {
            int dice_one = StdRandom.uniform(1,7);
            int dice_two = StdRandom.uniform(1,7);
            int sum = dice_one + dice_two;
            experiment[sum] = experiment[sum] + 1;

            if ( N%2 == 0 && N != 0)
            {
                //check probability
                double probable_error = 0.0;
                for (int i=0; i < prob.length; i++)
                {
                    double experiment_prob = (float)experiment[i] / N;
                    double error = Math.abs(experiment_prob - prob[i]);

                    probable_error = probable_error + error;
                }
                StdOut.println(N + " times experiment, all error is " + probable_error);
                if (probable_error <= 0.001) break;
            }
            N += 1;
        }
        StdOut.println("final experiment times is : " + N);
    }

    public static boolean circularRotation(String s, String t)
    {
        /* 
            home work 1.2.6
            return  : true if s is the circular rotation of t;
        */
        return (s.length() == t.length()) && (s.concat(s).indexOf(t) >= 0);
    }


    public static String mystery3(String s)
    {
        int N = s.length();
        if ( N <= 1) return s;
        String a = s.substring(0, N/2);
        String b = s.substring(N/2, N);
        return mystery3(a) + mystery3(b);
    }


    public static boolean parentheses(String s)
    {
        /* 
            home work 1.3.4
            return  : whether the parentheses are symmetrical
        */

        Stack<String> stack = new Stack<String>();
        for(int i = 0; i < s.length(); i++)
        {
            String tmp_s = s.substring(i,i+1);

            if (tmp_s.equals("(") || tmp_s.equals("[") || tmp_s.equals("{"))    stack.push(tmp_s);
            else if (tmp_s.equals(")"))
            {
                String previous = stack.pop();
                if ( previous.equals("(") == false){
                    return false;
                }
            }
            else if (tmp_s.equals("]"))
            {
                String previous = stack.pop();
                if ( previous.equals("[") == false){
                    return false;
                }
            }
            else if (tmp_s.equals("}"))
            {
                String previous = stack.pop();
                if ( previous.equals("{") == false){
                    return false;
                }
            }
        }
        if (stack.size() == 0) return true;
        else                   return false;
    }

    public static void prefix2infix(String s)
    {
        /* 
            home work 1.3.9
            return : Supplement the expression lacking left parenthesis
        */

        String[] charset = s.split(" ");
        Stack<String> ops = new Stack<String>();
        Stack<String> vals = new Stack<String>();
        for ( int i = 0; i < charset.length; i++)
        {
            if ( charset[i].equals("+") || charset[i].equals("-") || charset[i].equals("*") || charset[i].equals("/"))
            {
                ops.push(charset[i]);
            }
            else if ( charset[i].equals(")"))
            {
                String v1 = vals.pop();
                String v2 = vals.pop();
                String o = ops.pop();
                vals.push("(" + v1 + o + v2 + ")");
            }
            else vals.push(charset[i]);
        }
        StdOut.println(vals.pop());
    }


    public static void Infix2Postfix(String s)
    {
        /* 
            home work 1.3.10
            return : infix to postfix
        */

        String[] charset = s.split(" ");
        Stack<String> result = new Stack<String>();
        for ( int i = 0; i < charset.length; i++)
        {
            if (charset[i].equals("+") || charset[i].equals("-") || charset[i].equals("*") || charset[i].equals("/"))
            {
                result.push(charset[i]);
            }
            else if ( charset[i].equals(")")) 
            {
                StdOut.print(result.pop() + " ");
            }
            else if ( charset[i].equals("("))
            {
                StdOut.print("");
            }
            else
            {
                StdOut.print(charset[i] + " ");
            }
        }
        StdOut.println();
    }

    public static int FourNum(int[] a)
    {
        /* 
            home work 1.4.14
            return : the num of four values and four value of 0
        */
        int N = a.length;
        int cnt = 0;
        for (int i = 0; i < N; i++) 
        {
            for (int j = i + 1; j < N; j++) 
            {
                for (int k = j + 1; k < N; k++)
                {
                    for (int l = k + 1; l < N; l++)
                    {
                        if(a[i] + a[j] + a[k] + a[l] == 0)
                            cnt++;
                    }
                }
            }
        }
        return cnt;
    }

    public static void MinimumDifference(int[] a)
    {
        /* 
            home work 1.4.16
            return : the two number of the smallest difference in the array
        */
        Arrays.sort(a);
        int second = a[1];
        int first = a[0];
        int d_value = first - second;
        StdOut.println("two num is " + second  + " and " + first + ", d-value is " + d_value);
    }

    public static void MaximumDifference(int[] a)
    {
        /* 
            home work 1.4.17
            return : the two number of the smallest difference in the array
        */
        Arrays.sort(a);
        int big = a[a.length - 1];
        int small = a[0];
        int d_value = big - small;
        StdOut.println("two num is " + big  + " and " + small + ", d-value is " + d_value);
    }

    public static void LocalMinmum(int[] a)
    {
        /* 
            home work 1.4.18
            return : a[i] < a[i-1] && a[i] < a[i+1]， find a i
        */
        int mid1 = (a.length - 1) / 2;
        int mid2 = (a.length - 1) / 2;
        while(mid1 > 0 || mid2 < a.length)
        {
            if (a[mid1] < a[mid1 - 1] && a[mid1] < a[mid1 + 1])
            {
                StdOut.println("local min is " + a[mid1-1] + " " + a[mid1] + " " + a[mid1+1]);
                break;
            }

            else if (a[mid2] < a[mid2 - 1] && a[mid2] < a[mid2 + 1])
            {
                StdOut.println("local min is " + a[mid2-1] + " " + a[mid2] + " " + a[mid2+1]);
                break;
            }
            else
            {
                mid1 = mid1 / 2;
                mid2 = (a.length - 1 - mid2) / 2; 
            }
        }
    }

    public static boolean BitonicExist(int[] a, int key)
    {
        /*
            home work 1.4.20
            return : true if key in a
        */
        int max_index = BitonicMax.Max(a, 0, a.length - 1);
        int leftside = BinarySearchAscending(a, key, 0, max_index);
        int rightside = BinarySearchDescending(a, key, max_index, a.length - 1);
        if (leftside != -1 || rightside != -1) return true;
        else                                   return false;
    }

    public static int BinarySearchAscending(int[] a, int key, int lo, int hi)
    {
        while(lo <= hi)
        {
            int mid = lo + (hi - lo) / 2;
            if      (a[mid] > key)      lo = mid + 1;
            else if (a[mid] < key)      hi = mid - 1;
            else                        return mid;
        }
        return -1;
    }

    public static int BinarySearchDescending(int[] a, int key, int lo, int hi)
    {
        while(lo < hi)
        {
            int mid = lo + (hi - lo) / 2;
            if      (a[mid] > key)      lo = mid + 1;
            else if (a[mid] < key)      hi = mid - 1;
            else                        return mid;
        }
        return -1;
    }

    public static String[] dedup(String[] a)
    {
        /*
            home work 2.5.4
            return : sort and repeat
        */
        QuickSort3Way.sort(a);
        int number = 0;
        for(int i = 0; i < a.length; i++){
            if (a[i] != a[number]){
                number++;
                a[number] = a[i];
            }
        }

        number++;

        String[] b = new String[number];
        for (int i = 0; i < number; i++)
            b[i] = a[i];
        return b;
    }

    private static int partition(String[] a, int lo, int hi)
    {
        int i = lo;             // left index
        int j = hi + 1;         // right index
        String v = a[lo];
        while(true)
        {
            while(less(a[++i], v)) if (i == hi) break;
            while(less(v, a[--j])) if (j == lo) break;
            if (i >= j) break;
            exch(a, i, j);
        }
        exch(a, lo, j);
        return j;
    }

    private static boolean less(String v, String w)
    {
        return v.compareTo(w) < 0;
    }

    private static void exch(String[] a, int i, int j)
    {
        String t = a[i];
        a[i] = a[j];
        a[j] = t;
    }

    public static String select(String[] a, int k, int lo, int hi){
        /*
            home work 2.5.6
            return : first k small element
        */
        StdRandom.shuffle(a);
        while(hi > lo){
            int j = partition(a, lo, hi);
            if      (j == k) return a[k];
            else if (j > k) select(a, k, lo, j - 1);
            else if (j < k) select(a, k, j + 1, hi);
        }
        return a[k];
    }

    public static void frequency(String[] a){
        /*
            home work 2.5.8
            print : string statistics
        */
        Arrays.sort(a);
        int n = a.length;

        Record[] records = new Record[n];
        String word = a[0];
        int freq = 1;
        int m = 0;
        for (int i = 1; i < n; i++) {
            if(!a[i].equals(word)){
                records[m++] = new Record(word, freq);
                word = a[i];
                freq = 0;
            }
            freq++;
        }

        records[m++] = new Record(word, freq);
        Arrays.sort(records, 0, m);

        StdOut.println(records[m-1]);
        StdOut.println(records[m-2]);
        StdOut.println(records[m-3]);
        //for (int i = m-1; i >= 0; i--)
        //    StdOut.println(records[i]);
    }

    public static void main(String[] args)
    {
        String[] a = StdIn.readAllStrings();
        frequency(a);
    }
}
