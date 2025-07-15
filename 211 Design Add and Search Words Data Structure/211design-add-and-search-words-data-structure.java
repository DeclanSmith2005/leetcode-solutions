class WordDictionary {
    HashMap<Character, WordDictionary> Node; 
    boolean endWordHere;

    public WordDictionary() {
        Node = new HashMap<Character, WordDictionary>(100);
        endWordHere = false;
    }
    
    public void addWord(String word) {
         if (word.length() == 0){
            endWordHere = true;
            return;
        }
        if (Node.containsKey(word.charAt(0))){
            Node.get(word.charAt(0)).addWord(word.substring(1));
        }
        else{
            WordDictionary child = new WordDictionary();
            Node.put(word.charAt(0), child);
            child.addWord(word.substring(1));
        }
    }
    
    public boolean search(String word) {
        if (word.length() ==1 && word.charAt(0) == '.'){
            for (char c : Node.keySet()){
                if ( Node.get(c).endWordHere == true){
                    return true;
                }
            }
            return false;
        }
        if (word.length() == 1 && (Node.containsKey(word.charAt(0)))){
            if ( Node.get(word.charAt(0)).endWordHere == true ){
                return true;
            }
            else{
                return false;
            }
        }
        if ( word.charAt(0) == '.'){
            for (char c : Node.keySet()){
                if (Node.get(c).search(word.substring(1)) == true){
                    return true;
                }
            }
            return false;
        }
        if (Node.containsKey(word.charAt(0))){
            return Node.get(word.charAt(0)).search(word.substring(1));
        }
        else{
            return false;
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */