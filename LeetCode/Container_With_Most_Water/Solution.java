class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int lo = 0;
        int hi = height.length - 1;
        int temp;
        while(lo < hi){
            temp = Math.min(height[hi], height[lo]) * (hi - lo);
            if (temp > maxArea)
                maxArea = temp;
            if (height[hi] > height[lo])
                lo++;
            else
                hi--;
        }
        return maxArea;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] h = {2, 3, 10, 5, 7, 8, 9};
        System.out.println(s.maxArea(h));
    }
}