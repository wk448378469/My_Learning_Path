import java.util.Arrays;
import java.util.Comparator;

class Solution {

    private class LargerNumberComparator implements Comparator<String>{
        @Override
        public int compare(String a, String b){
            String order1 = a + b;
            String order2 = b + a;
            return order2.compareTo(order1);
        }
    }

    public String largestNumber(int[] nums) {
        String[] asStrs = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            asStrs[i] = String.valueOf(nums[i]);
        }

        Arrays.sort(asStrs, new LargerNumberComparator());

        if (asStrs[0].equals("0")) {
            return "0";
        }

        StringBuffer largestNumberStr = new StringBuffer();
        for (String s: asStrs) {
            largestNumberStr.append(s);
        }
        return largestNumberStr.toString();
    }

    public static void main(String[] args) {
        int[] input = new int[]{3,30,34,5,9};
        Solution s = new Solution();
        String result = s.largestNumber(input);
        System.out.println(result);
    }
}