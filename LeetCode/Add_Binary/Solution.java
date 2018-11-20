class Solution {
    public String addBinary(String a, String b) {
        StringBuilder s = new StringBuilder();
        int c = 0, i = a.length() - 1, j = b.length() - 1;

        while(i >= 0 || j >= 0 || c == 1)
        {
            int sum = c;
            if (i >= 0) sum += a.charAt(i--) - '0';
            if (j >= 0) sum += b.charAt(j--) - '0';
            s.append(sum%2);
            c = sum / 2;
        }
        
        if (c != 0) s.append(c);
        return s.reverse().toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.addBinary("101", "101101"));
    }
}