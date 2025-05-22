class Solution {


    boolean start ( int i, int[]gas, int[]cost){
        int start = i;
        int gasVal = 0;
        int n = gas.length;
        int dist = 0;
        int gain = gas[i] - cost[i];
        if (start == 0 && gain == 0 && n-1 == 0){
            return true;
        }
        if (gain < 1){
            return false;
        }
        while ( dist < n){
            gain = gas[i] - cost[i];
            if (gain + gasVal >= 0 ){
                dist++;
                i++;
                i %= n;
                gasVal += gain;
            }
            else{
                return false;
            }
        }
        return true;
    }
    
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int i = 0;
        while (true){
            if (i == gas.length){
                return -1;
            }
            boolean check = start ( i, gas, cost);
            if (check == true){
                return i;
            }
            i++;
        }

    }
}