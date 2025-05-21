class RandomizedSet {    
    
    ArrayList<Integer> list = new ArrayList<>();
    HashMap<Integer, Integer> indexMap = new HashMap<>();

    public RandomizedSet() {
        
    }
    
    public boolean insert(int val) {
        if (indexMap.containsKey(val)) {
            return false;
        } else {
            list.add(val);
            indexMap.put(val, list.size() - 1); 
            return true;
        }
    }

    public boolean remove(int val) {
        val = (Integer) val;
        Integer index = indexMap.get(val);
        if (index == null) return false;

        int lastIndex = list.size()-1;
        Integer lastElement = list.get(lastIndex);

        list.set(index, lastElement);
        indexMap.put(lastElement, index);

        list.remove(lastIndex);
        indexMap.remove(val);

        return true;
    }
    
    public int getRandom() {
        Random random = new Random();
        return list.get(random.nextInt(list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */