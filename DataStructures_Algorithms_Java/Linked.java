import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import java.util.Iterator;


class Node<Item>
{
    Item item;
    Node<Item> next;
    public Node(Item data)
    {
        this.item = data;
    }
}

public class Linked<Item> implements Iterable<Item>
{
    private Node<Item> first = null;
    private Node<Item> last = null;
    private int N = 0;


    public boolean isEmpty()
    {
        return N == 0;
    }

    public int size()
    {
        return N;
    }

    public void addFirst(Node<Item> node)
    {
        Node<Item> newNode = new Node<Item>(node.item);
        if ( first == null) last = newNode;
        newNode.next = first;
        first = newNode;
        N++;
    }

    public void addLast(Node<Item> node)
    {
        Node<Item> newNode = new Node<Item>(node.item);
        if ( first == null) 
        {
            first = newNode;
            last = newNode;
        }
        else
        {
            last.next = newNode;
            last = newNode;
        }
        N++;
    }

    public Item removeFirst()
    {
        Item item = first.item;
        if ( first.next == null) last = null;
        first = first.next;
        N--;
        return item;
    }


    public Item removeLast()
    {
        /*
            home work 1.3.19
            remove the last node;
        */
        if ( isEmpty()) return null;
        Item item = null;
        for (Node<Item> current = first; current != null; current = current.next)
        {
            if ( current.next.next == null)
            {
                item = current.next.item;
                current.next = null;
                last = current;
                N--;
            }
        }
        return item;
    }


    public Item delete(int k)
    {
        /*
            home work 1.3.20
            remove the index k node if exit 
        */
        if           ( k < 1)  throw new Error(" k > 0 ");
        else if      ( k > N)  return null;
        else if      ( k== 1)  return removeFirst();
        else if      ( k== N)  return removeLast();
        else 
        {
            Node<Item> current = first;
            Item item = null;
            for (int i = 1; i <= N; i++)
            {
                if ( i == k - 1)
                {
                    item = current.next.item;
                    current.next = current.next.next;
                    N--;
                }
                current = current.next;
            }
            return item;
        }
    }


    public boolean find(Linked link, Item item)
    {
        /*
            home work 1.3.21
            whether item is in link
        */

        Node currentNode = link.first;
        while(currentNode.next != null)
        {
            if (currentNode.item == item) return true;
            currentNode = currentNode.next;
        }
        return false;
    }



    public void removeAfter(Node<Item> node)
    {
        if      ( first == null) return;
        else if ( first == node) 
        {
            first = null;
            last = null;
            N = 0;
        }
        else
        {
            Node currentNode = first;
            int remaindNum = 1;
            while(currentNode.next != null)
            {
                if ( currentNode.next == node)
                {
                    currentNode.next = null;
                    last = currentNode;
                    N = remaindNum;
                    break;
                }
                currentNode = currentNode.next;
                remaindNum++;
            }
        }
    }

    public void remove(Linked link, Item item)
    {
        if ( link.first == null) return;
        Node parentNode = link.first;
        while ( parentNode.next != null)
        {
            if ( parentNode == link.first && parentNode.item == item)
            {
                link.first = link.first.next;

            }else
            {
                if ( parentNode.next.item == item)
                {
                    parentNode.next = parentNode.next.next;
                }
            }
            parentNode = parentNode.next;
        }
    }

/*
    public Item removeFirst()
    {
        Item item = first.item;
        if ( first.next == null) last = null;
        first = first.next;
        N--;
        return item;
    } */

    public Iterator<Item> iterator()
    {
        return new ListIterator<Item>(first);
    }

    private class ListIterator<Item> implements Iterator<Item>
    {
        private Node<Item> current;

        public ListIterator(Node<Item> first)
        {
            current = first;
        }

        public boolean hasNext()
        {
            return current != null;
        }

        public void remove(){ /*not supported!! */}

        public Item next()
        {
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    public static void main(String[] args) 
    {
        Linked<String> linked = new Linked<String>();
        Node<String> a = new Node<String>("a");
        Node<String> b = new Node<String>("b");
        Node<String> c = new Node<String>("c");
        Node<String> d = new Node<String>("d");
        Node<String> e = new Node<String>("e");
        Node<String> f = new Node<String>("f");
        linked.addLast(b);
        linked.addFirst(c);
        linked.addLast(a);
        linked.addLast(d);
        linked.addFirst(e);
        StdOut.println("current order: ");
        for(String l : linked)
        {
            StdOut.print(l + " ");
        }


        StdOut.println();
        StdOut.println("before remove first item: ");
        linked.removeFirst();
        for(String l : linked)
        {
            StdOut.print(l + " ");
        }


        StdOut.println();
        StdOut.println("before remove last item: ");
        linked.removeLast();
        for(String l : linked)
        {
            StdOut.print(l + " ");
        }


        linked.addLast(f);
        StdOut.println();
        StdOut.println("before add last item again: ");
        for(String l : linked)
        {
            StdOut.print(l + " ");
        }

        linked.delete(3);
        StdOut.println();
        StdOut.println("remove index 3 item: ");
        for(String l : linked)
        {
            StdOut.print(l + " ");
        }

        StdOut.println();
        StdOut.println("a in linked ? " + linked.find(linked, "a"));

        Node<String> h = new Node<String>("h");
        linked.addLast(h);
        Node<String> i = new Node<String>("i");
        linked.addLast(i);
        linked.removeAfter(b);
        StdOut.println();
        StdOut.println("add two node and remove after f:");
        for(String l : linked)
        {
            StdOut.print(l + " ");
        }
        StdOut.println();
        StdOut.println("current size = " + linked.size());

        StdOut.println();
        linked.addLast(b);
        linked.addLast(b);
        linked.addLast(c);
        for(String l : linked)
        {
            StdOut.print(l + " ");
        }

        linked.remove(linked, "b");
        StdOut.println();
        for(String l : linked)
        {
            StdOut.print(l + " ");
        }
    }
}