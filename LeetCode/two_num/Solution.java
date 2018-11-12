import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mydict = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            int another = target - nums[i];
            if (mydict.containsKey(another)) {
                return new int[]{mydict.get(another), i};
            }
            mydict.put(nums[i], i);
        }
        return new int[]{-1, -1};
    }

    public static void main(String[] args) {
        int[] nums = new int[]{2,7,11,15};
        int target = 9;
        Solution s = new Solution();
        int[] result = s.twoSum(nums, target);
        for (int i : result) {
            System.out.println(i);
        }
    }
}