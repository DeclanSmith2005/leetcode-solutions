class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        int[] prefix = new int[nums.length];
        prefix[0] = 1;
        answer[nums.length-1] = 1;
        int pref = 1;
        int ans = 1;
        for (int i = 1; i< nums.length; i++){
            pref *= nums[i-1];
            prefix[i] = pref;
        }


        for (int i = nums.length - 1; i >= 0; i--){
            if (i!= nums.length-1){
                ans = ans*nums[i+1];
            }
            answer[i] = ans*prefix[i];
        }

        return answer;
    }
}