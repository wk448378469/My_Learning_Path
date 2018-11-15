import java.util.HashSet;
import java.util.Set;

class Solution {
    public int numJewelsInStones(String J, String S) {
        int num = 0;
        Set myset = new HashSet();

        for (char c : J.toCharArray()) {
            myset.add(c);
        }

        for (char c : S.toCharArray()) {
            if (myset.contains(c))
                num++;
        }
        return num;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.numJewelsInStones("aA", "aAAbbbb"));
    }
}