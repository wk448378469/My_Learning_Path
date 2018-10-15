public class Record implements Comparable<Record>{
    private final String name;
    private final int freq;

    public Record(String name, int freq){
        this.name = name;
        this.freq = freq;
    }

    public int compareTo(Record that){
        if (this.freq > that.freq) return +1;
        if (this.freq < that.freq) return -1;
        return 0;
    }

    public String toString() {
        return name + " / " + freq + " times";
    }
}