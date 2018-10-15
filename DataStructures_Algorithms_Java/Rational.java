import edu.princeton.cs.algs4.StdOut;

public class Rational
{
    // Calculating rational number
    // home work: 1.2.16-1.2.17

    private final int numerator;
    private final int demoninator;

    public Rational(int numerator, int demoninator)
    {
        if (demoninator == 0) throw new Error(" demoninator should not be 0 !");
        int gcd = euclid(numerator, demoninator);
        this.numerator = numerator / gcd;
        this.demoninator = demoninator / gcd;
    }

    private static int euclid(int n, int m)
    {
        /* 
            home work 1.1.24
            return  : the maximum common divisor of m and n
        */
        int max;
        int min;
        if (n > m)          { max = Math.abs(n); min = Math.abs(m);}
        else if (n < m)     { max = Math.abs(m); min = Math.abs(n);}
        else return n;

        if (min == 0){return max;}

        int p = max / min;
        int q = max % min;
        //StdOut.println(max + "=" + p + "*" + min + "+" + q);
        if (q == 0) {return min;}
        else return euclid(min, q);
    }

    public Rational plus(Rational b)
    {
        int numerator = this.numerator * b.demoninator + this.demoninator * b.numerator;
        int demoninator = this.demoninator * b.demoninator;
        int gcd = euclid(numerator, demoninator);
        return new Rational(numerator/gcd, demoninator/gcd);
    }

    public Rational minus(Rational b)
    {
        int numerator = this.numerator * b.demoninator - this.demoninator * b.numerator;
        int demoninator = this.demoninator * b.demoninator;
        int gcd = euclid(numerator, demoninator);
        return new Rational(numerator/gcd, demoninator/gcd);
    }

    public Rational times(Rational b)
    {
        int numerator = this.numerator * b.numerator;
        int demoninator = this.demoninator * b.demoninator;
        int gcd = euclid(numerator, demoninator);
        return new Rational(numerator/gcd, demoninator/gcd);
    }

    public Rational divides(Rational b)
    {
        if ( b.numerator == 0) throw new Error(" divisor should not be 0 !");
        int numerator = this.numerator * b.demoninator;
        int demoninator = this.demoninator * b.numerator;
        int gcd = euclid(numerator, demoninator);
        return new Rational(numerator/gcd, demoninator/gcd);
    }

    public boolean equals(Rational that)
    {
        if (this == that) return true;
        if (that == null) return false;
        if (this.getClass() != that.getClass()) return false;
        return (this.numerator == that.numerator && this.demoninator == that.demoninator);
    }

    public String toString()
    {
        return this.numerator + "/" + this.demoninator;
    }

    public static void main(String[] args) {
        Rational r1 = new Rational(6,9);
        Rational r2 = new Rational(2,3);

        Rational r3 = r1.plus(r2);
        StdOut.println(r1 + " + " + r2 + " = " + r3);

        Rational r4 = r1.minus(r2);
        StdOut.println(r1 + " - " + r2 + " = " + r4);

        Rational r5 = r1.times(r2);
        StdOut.println(r1 + " * " + r2 + " = " + r5);

        Rational r6 = r1.divides(r2);
        StdOut.println(r1 + " / " + r2 + " = " + r6);

        StdOut.println("r1 and r2 is equals? " + r1.equals(r2));
    }

}