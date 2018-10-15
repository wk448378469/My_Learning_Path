import edu.princeton.cs.algs4.BinaryStdIn;
import edu.princeton.cs.algs4.BinaryStdOut;

public class Genome
{
    private Genome(){}

    public static void compress(){
        Alphabet DNA = new Alphabet("ACTG");
        String s = BinaryStdIn.readString();
        int n = s.length();
        BinaryStdOut.write(n);

        for (int i = 0; i < n; i++) {
            int d = DNA.toIndex(s.charAt(i));
            BinaryStdOut.write(d, DNA.lgR());
        }
        BinaryStdOut.close();
    }

    public static void expand(){
        Alphabet DNA = new Alphabet("ACTG");
        int n = BinaryStdIn.readInt();
        int w = DNA.lgR();

        for (int i = 0; i < n; i++) {
            char c = BinaryStdIn.readChar(w);
            BinaryStdOut.write(DNA.toChar(c));
        }
        BinaryStdOut.close();
    }

    public static void main(String[] args) {
        if      (args[0].equals("-")) compress();
        else if (args[0].equals("+")) expand();
        else throw new IllegalArgumentException();
    }
}