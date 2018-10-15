public class Matrix
{
    public static double dot(double[] x, double [] y)
    {
        /*
            return dot product of x and y
        */
        if (x.length != y.length) {throw new IllegalArgumentException("x and y length not equal!");}

        double sum = 0.0;
        for (int i = 0 ; i < x.length; i++)
        {
            sum += x[i]*y[i];
        }
        return sum;
    }

    private static double[] col(double[][] x, int index)
    {
        /*
            return index column of x
        */
        double [] col = new double[x.length];
        for (int i = 0; i < x.length; i++)
        {
            col[i] = x[i][index];
        }
        return col;
    }

    public static double[][] mult(double[][] a, double[][] b)
    {
        /*
            return product of a and b
        */
        if (a[0].length != b.length) {throw new IllegalArgumentException("a.col and b.row length not equal!");}

        double [][] result = new double[a.length][b[0].length];

        for (int i = 0; i < a.length; i ++ )
        {
            for (int j = 0; j < b[0].length; j++)
            {
                result[i][j] = dot(a[i], col(b,j));
            }
        }
        return result;
    }


    public static double[][] transpose(double[][] a)
    {
        /*
            return transpose of a
        */
        double [][] result = new double[a[0].length][a.length];
        for (int i = 0; i < a.length; i++)
        {
            for (int j = 0; j < a[i].length; j++)
            {
                result[j][i] = a[i][j];
            }
        }
        return result;
    }


    public static double[] mult(double[][] a, double[] x)
    {
        /*
            return product of a and x
        */
        if (a[0].length != x.length) { throw new IllegalArgumentException("a.col and x.length not equal!");}

        double [] result = new double[a.length];
        for (int i = 0; i < result.length; i++)
        {
            result[i] = dot(a[i], x);
        }
        return result;
    }

    public static double[] mult(double[] y, double[][] a)
    {
        /*
            return product of y and a
        */
        if (a.length != y.length) { throw new IllegalArgumentException("a.col and y.length not equal!");}
        double [] result = new double[a[0].length];
        for (int i = 0; i < result.length; i++)
        {
            result[i] = dot(y, col(a,i));
        }
        return result;
    }

    public static void main(String[] args) {
        
    }
}