import edu.princeton.cs.algs4.StdOut;

public class PhoneNumber
{
    private final int area;
    private final int exch;
    private final int ext;

    public PhoneNumber(int area, int exch, int ext){
        this.area = area;
        this.exch = exch;
        this.ext = ext;
    }

    @Override
    public boolean equals(Object that){
        if (that == this) return true;
        if (that == null) return false;
        if (that.getClass() != this.getClass()) return false;
        PhoneNumber it = (PhoneNumber) that;
        return (this.area == it.area) && (this.exch == it.exch) && (this.ext == it.ext);
    }

    @Override
    public String toString(){
        return String.format("(%03d) %03d-%04d", area, exch, ext);
    }

    @Override
    public int hashCode(){
        return 31 * (area + 31 * exch) + ext;
    }

    public static void main(String[] args) {
        PhoneNumber a = new PhoneNumber(609, 258, 4555);
        PhoneNumber b = new PhoneNumber(215, 873, 2322);
        String x = "aasdas";
        StdOut.println("a = " + a);
        StdOut.println("b = " + b);
        StdOut.println("hash code of a = " + a.hashCode());
        StdOut.println("hash code of b = " + b.hashCode());
        StdOut.println(x.hashCode());
    }
}