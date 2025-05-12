import java.util.*;


class Solution {
    public int majorityElement(int[] nums) {
        int number = nums[0];
        int count = 1;
        for (int i = 1; i<nums.length; i++){
             if (count == 0){
                number = nums[i];
            }
            if (nums[i] == number){
                count++;
            }
            else{
                count--;
            }
           
        }

        return number;
    }
}