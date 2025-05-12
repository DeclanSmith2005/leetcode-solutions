class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;
        boolean twice = false; // primed if already one duplicate
        for (int i =1; i<nums.length; i++){
            if (nums[i] != nums[k] ){
                nums[++k] = nums[i];
                twice = false;
            }
            else if (twice == false){
                nums[++k] = nums[i];
                twice = true;
            }
        }
        return ++k;
    }
}