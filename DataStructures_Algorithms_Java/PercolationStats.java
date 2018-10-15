import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats{
    private double[] threshold;
    private double constant = 1.96;
    private double mean_;
    private double stddev_;
    private double confidenceLo_;
    private double confidenceHi_;


    public PercolationStats(int n, int trials){
        //perform trials independent experiments on an n*n grid
        if(n <= 0 || trials <= 0){
            throw new IllegalArgumentException("n and trials must be greater than 0");
        }
        else{
            threshold = new double[trials];
            for(int i = 0 ; i < trials; i++){
                Percolation p = new Percolation(n);
                while (true) {
                    int row = StdRandom.uniform(1, n + 1);
                    int col = StdRandom.uniform(1, n + 1);
                    p.open(row, col);
                    if (p.percolates()) {
                        threshold[i] = (double)p.numberOfOpenSites() / (n * n);
                        break;
                        }
                    }
                }
            mean_ = _mean();
            stddev_ = _stddev();
            confidenceLo_ = _confidenceLo();
            confidenceHi_ = _confidenceHi();
            }
    }

    private double _stddev(){
        return StdStats.stddev(threshold);
    }

    public double stddev(){
        //sample standard deviation of percolation threshold
        return stddev_;
    }

    private double _mean(){
        return StdStats.mean(threshold);
    }

    public double mean(){
        // sample mean of percolation threshold
        return mean_;
    }

    private double _confidenceLo(){
        return mean_ - (constant * stddev_) / Math.sqrt(threshold.length);
    }

    public double confidenceLo(){
        // low endpoint of 95% confidence interval
        return confidenceLo_;
    }

    private double _confidenceHi(){
        //high endpoint of 95% confidence interval
        return mean_ + (constant * stddev_) / Math.sqrt(threshold.length);
    }

    public double confidenceHi(){
        //high endpoint of 95% confidence interval
        return confidenceHi_;
    }

    public static void main(String[] args) {
        PercolationStats p = new PercolationStats(200, 100);
        System.out.println("mean                      = " + p.mean());
        System.out.println("stddev                    = " + p.stddev());
        System.out.println("95%% confidence Interval  = [" + 
                    p.confidenceLo() + ", " +  p.confidenceHi() + "]");
    }
}