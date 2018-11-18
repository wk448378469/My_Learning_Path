import java.util.Stack;

public class Solution {

    private Stack<Pair> stack = new Stack<Pair>();
    private int n = 0;

    /** initialize your data structure here. */
    public Solution() {}
    
    public void push(int x) {
        if (n == 0 || x <= stack.peek().currentMinValue)
            stack.push(new Pair(x, x));
        else
            stack.push(new Pair(x, stack.peek().currentMinValue));
        n++;
    }
    
    public void pop() {
        stack.pop();
        n--;
    }
    
    public int top() {
        return stack.peek().key;
    }
    
    public int getMin() {
        return stack.peek().currentMinValue;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        s.push(-10);
        s.push(14);
        System.out.println(s.getMin());
        System.out.println(s.getMin());
        s.push(-20);
        System.out.println(s.getMin());
        System.out.println(s.getMin());
        System.out.println(s.top());
        System.out.println(s.getMin());
        s.pop();
        s.push(10);
        s.push(-7);
        System.out.println(s.getMin());
        s.push(-7);
        s.pop();
        s.pop();
        System.out.println(s.getMin());
        s.pop();
    }
}

class Pair
{
    public int key;
    public int currentMinValue;
    public Pair(int key, int currentMinValue)
    {
        this.key = key;
        this.currentMinValue = currentMinValue;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * Solution obj = new Solution();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */

