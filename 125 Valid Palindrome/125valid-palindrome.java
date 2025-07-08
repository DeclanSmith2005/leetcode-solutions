class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        int i= 0;
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                sb.append(Character.toLowerCase(c));
            }
        }
        int k= sb.length();
        if ( s.length() != 0 && k == 0){
            return true;
        }
        int n = k;
        if ( k == 0){
            return false;
        }
        k--;
        boolean check = true;
        while (sb.charAt(i) == sb.charAt(k) && i < k ){
            char lower = sb.charAt(i);
            char upper = sb.charAt(k);
            i++;
            k--; 
        }
        if (sb.charAt(i) != sb.charAt(k)){
            check = false;
        }
        return check;
    }
    
}