class MedianFinder {
    ArrayList<Integer> nums;
    int len;
    public MedianFinder() {
        nums = new ArrayList<>();
    }
    
    public void addNum(int num) {
        if (len == 0 ){
            nums.add(num);
            len+=1;
            return; 
        }
        int left = 0;
        int right= len-1;
        int mid=0;
        len+=1;
        while (left <= right){
            mid = (int) Math.floor((left + right)/2);
            if (nums.get(mid) == num){
                nums.add(mid,num);
                return;
            }
            if (num < nums.get(mid)){
                right = mid-1;
            }
            else {
                left = mid +1;
            }
        }
        if (nums.get(mid)> num){
            nums.add(mid, num);
        }
        else{
            nums.add(mid+1,num);
        }
        return; 
            
    }
    
    public double findMedian() {
        if (len%2 == 0){
            return (double)(nums.get(len/2) + nums.get((len/2)-1))/2;
        } 
        else{
            return (double)(nums.get((int)Math.floor(len/2)));
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */