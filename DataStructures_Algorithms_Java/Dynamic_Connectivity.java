import java.util.Arrays;

/*
    UF: 
        union find
        pass

    QuickFind:
        check whether two index are connected, time complexity is always O(n) 
        unicon two index, time complexity is always O(1)

    QuickUnion:
        check whether two index are connected, time complexity is always O(n) 
        unicon two index, the worst time complexity is O(n)

    WeightedQuickUnion:
        check whether two index are connected, time complexity is always O(lg(n)) 
        unicon two index, the worst time complexity is O(lg(n)) 

    PathCompressionWeightedQuickUnionUF:
        is batter tran WeightedQuickUnion, but the time complexity is too complicated calc
*/

public class Dynamic_Connectivity{
    public static void main(String[] args) {
        QuickFindUF uf = new QuickFindUF(10);
        uf.union(0, 1);
        uf.union(3, 7);
        uf.union(3, 1);
        System.out.println("0 and 7 is connected ? " + uf.connected(0,7));

        QuickUnionUF uf_1 = new QuickUnionUF(20);
        uf_1.union(3, 4);
        uf_1.union(3, 9);
        System.out.println("4 and 9 is connected ? " + uf_1.connected(4,9));

        WeightedQuickUnionUF uf_2 = new WeightedQuickUnionUF(20);
        uf_2.union(3,5);
        uf_2.union(5,8);
        uf_2.union(7,2);
        uf_2.union(1,2);
        uf_2.union(10,3);
        System.out.println("5 and 10 is connected ? " + uf_2.connected(5,10));
    }
}


class QuickFindUF{
    private int[] id;

    public QuickFindUF(int N){
        id = new int[N];
        for(int i=0; i<N; i++){
            id[i] = i;
        }
    }

    public boolean connected(int p, int q){
        return id[p] == id[q];
    }

    public void union(int p, int q){
        int pid = id[p];
        int qid = id[q];
        for(int i=0; i<id.length; i++){
            if(id[i] == pid){
                id[i] = qid;
            }
        }
    }
}



class QuickUnionUF
{
    private int[] id;

    public QuickUnionUF(int N)
    {
        id = new int[N];
        for(int i=0; i<N; i++){
            id[i] = i;
        }
    }

    public int root(int i)
    {
        while(i != id[i])
        {
            i = id[i];
        }
        return i;
    }

    public boolean connected(int p, int q)
    {
        return root(p) == root(q);
    }

    public void union(int p, int q)
    {
        int i = root(p);
        int j = root(q);
        id[i] = j;
    }
}


class WeightedQuickUnionUF
{
    private int[] sz;
    private int[] id;

    public WeightedQuickUnionUF(int N)
    {
        id = new int[N];
        sz = new int[N];
        for(int i=0; i<N; i++){
            id[i] = i;
            sz[i] = 1;
        }
    }

    public int root(int i)
    {
        while(i != id[i])
        {
            i = id[i];
        }
        return i;
    }

    public boolean connected(int p, int q)
    {
        return root(p) == root(q);
    }


    public void union(int p, int q)
    {
        int i = root(p);
        int j = root(q);
        if(i==j)
            {
                return;
            }
        if(sz[i] < sz[j]){
            id[i] = j;
            sz[j] += sz[i];
        }else{
            id[j] = i;
            sz[i] += sz[j];
        }
    }
}


class PathCompressionWeightedQuickUnionUF
{
    private int[] sz;
    private int[] id;

    public PathCompressionWeightedQuickUnionUF(int N)
    {
        id = new int[N];
        sz = new int[N];
        for(int i=0; i<N; i++){
            id[i] = i;
            sz[i] = 1;
        }
    }

    public int root(int i)
    {
        while(i != id[i])
        {
            id[i] = id[id[i]];
            i = id[i];
        }
        return i;
    }

    public boolean connected(int p, int q)
    {
        return root(p) == root(q);
    }


    public void union(int p, int q)
    {
        int i = root(p);
        int j = root(q);
        if(i==j)
            {
                return;
            }
        if(sz[i] < sz[j]){
            id[i] = j;
            sz[j] += sz[i];
        }else{
            id[j] = i;
            sz[i] += sz[j];
        }
    }
}