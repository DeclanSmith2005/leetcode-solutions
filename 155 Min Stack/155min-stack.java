class MinStack {
    private ArrayList<Integer> myStack;
    private ArrayList<Integer> minList;
    private int top = -1;
    private Integer min = null; 

    public MinStack() {
        myStack = new ArrayList<>();
        minList = new ArrayList<>();
    }
    
    public void push(int val) {
        top++;
        myStack.add(top, val);
        if (min == null){
            min = val;
        }
        else{
            min = Math.min(minList.get(top-1), val);
        }
        minList.add(top, min);
    }
    
    public void pop() {
        myStack.remove(top);
        minList.remove(top);
        top--;
        if (top < 0){
            min = null;
        }
    }
    
    public int top() {
        return myStack.get(top);
    }
    
    public int getMin() {
        return minList.get(top);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */