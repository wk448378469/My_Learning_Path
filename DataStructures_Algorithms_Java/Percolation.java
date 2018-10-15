import edu.princeton.cs.algs4.WeightedQuickUnionUF;


public class Percolation {
    private int siteLength;
    private boolean[] status;
    private WeightedQuickUnionUF uf;

    public Percolation(int n){ 
        // create n*n grid, with all sites blocked
        if (n <= 0) {
            throw new IllegalArgumentException("n out of bounds");
        } else {
            // init data
            uf = new WeightedQuickUnionUF(n*n + 2);
            siteLength = n;
            status = new boolean[n*n + 2];
            status[0] = true;

            for (int i = 1; i <= n*n; i++) {
                // connect virtual top with first row
                if (i <= n) { uf.union(i, 0);}
                // connect virtual bottom with last row
                if (i > (n-1) * n) { uf.union(i, n*n+1);}
                status[i] = false;
            }
            status[n*n + 1] = true;
        }
    }

    private int xyTo1D(int i, int j) { 
        // mapping 2D coordinates to 1D coordinates
        if (i <= 0 || i > siteLength) { throw new IllegalArgumentException("i out of bounds");}
        if (j <= 0 || j > siteLength) { throw new IllegalArgumentException("j out of bounds");} 
        return (i - 1) * siteLength + j;
    }

    public void open(int row, int col){ 
        // open site(row,col) if it is not open already

        int index = xyTo1D(row, col);
        status[index] = true;

        // up site union
        if (row != 1 && isOpen(row-1, col)) { 
            uf.union(index, xyTo1D(row - 1, col));
        }

        // bottom site union
        if (row != siteLength && isOpen(row + 1, col)) { 
            uf.union(index, xyTo1D(row + 1, col));
        }

        // left site union
        if (col != 1 && isOpen(row, col - 1)) { 
            uf.union(index, xyTo1D(row, col -1));
        }

        // right site union
        if (col != siteLength && isOpen(row, col + 1)) { 
            uf.union(index, xyTo1D(row, col + 1));
        }
    }

    public boolean isOpen(int row, int col){ 
        // is site(row,col) open
        int index = xyTo1D(row, col);
        return status[index];
    }

    public boolean isFull(int row, int col){ 
        // is site(row,col) full?
        int index = xyTo1D(row, col);
        return isOpen(row, col) && uf.connected(index, 0);
    }

    public int numberOfOpenSites(){ 
        // number of open sites
        int n = 0;
        for (int i = 0; i < status.length; i++) { 
            if (status[i] == true) { n += 1;}
        }
        // delete virtual top and bottom 
        return n - 2;
    }

    public boolean percolates(){ 
        // does the system percolate?
        if (siteLength == 1) {
            return isOpen(1,1) && uf.connected(0, siteLength*siteLength + 1);
        }
        return uf.connected(0, siteLength*siteLength + 1);
    }

    public static void main(String[] args){ 
        // test
        Percolation p = new Percolation(3);
        p.open(1,3);
        p.open(2,3);
        p.open(3,3);
        p.open(3,1);
        System.out.println(p.isFull(3,1));
        System.out.println(p.percolates());
    }
}