import java.util.Stack;
import java.lang.Character;

class Solution {
    public int calculate(String s) {
        Stack<Integer> vals = new Stack<Integer>();
        int num = 0;
        char sign = '+';
        for (int i = 0; i < s.length(); i++) {
            if (Character.isDigit(s.charAt(i)))
                num = num*10 + s.charAt(i) - '0';
            if (!Character.isDigit(s.charAt(i)) && s.charAt(i) != ' ' || i == s.length()-1){
                if (sign == '-')
                    vals.push(-num);
                else if (sign == '+')
                    vals.push(num);
                else if (sign == '*')
                    vals.push(vals.pop() * num);
                else
                    vals.push(vals.pop() / num);

                sign = s.charAt(i);
                num = 0;
            }
        }
        int sum = 0;
        for (int i : vals) {
            sum += i;
        }
        return sum;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.calculate("14-3/2"));
    }
}