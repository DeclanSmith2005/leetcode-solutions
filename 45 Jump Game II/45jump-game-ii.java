class Solution {
    public int jump(int[] nums) {
        int n = nums.length-1;
        int index  = 0;
        int numJumps = 0;
        while (true){
            int myJump = nums[index];
            int best = myJump;
            int bestInd = 0;
            if (nums.length == 1){
                return 0;
            }
            if (myJump >= n-index){
                numJumps++;
                return numJumps;
            }
            if (myJump != 0){
                for (int i = 1; i <= myJump; i++){
                    if( nums[index + i] + i > best){
                        bestInd = i;                        
                        best = nums[index + i] + i;
                    }
                }
                if (bestInd != 0){
                    index += bestInd;
                    myJump = nums[index];
                    numJumps++;
                }
            }
        }
    }
}