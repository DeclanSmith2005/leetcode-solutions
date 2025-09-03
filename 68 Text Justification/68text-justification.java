class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        int i = 0;
        int difference;
        int standardAmt;
        int extraSpaces;
        int L = words.length;
        List<String> returnList = new ArrayList<>();
        StringBuilder sb = new StringBuilder("");
        List<Integer> spaceIndices = new ArrayList<>();

        while ( i < L){
            int k = 0;
            spaceIndices.clear();
            int numGaps=-1; 
            int length = 0;
            sb.setLength(0);
            int zeroInd = k+1;
            while(length < maxWidth && i < L){
                sb.append(words[i]);
                spaceIndices.add(length-1);
                numGaps++;
                i++;
                k++;
                length = sb.length();
                if ( length < maxWidth-1){
                    sb.append(" ");
                    length++;
                }
                else{
                    break;
                }
            }
            if (length > maxWidth){
                i--;
                numGaps--;
                k--;
                int temp = spaceIndices.get(k);
                sb.delete(temp, length);                                
                String trimmed = sb.toString().trim();
                sb.setLength(0); 
                sb.append(trimmed); 
                length = sb.length();
            }
            if ( numGaps >= 1 && i < L){
                difference = maxWidth - length;
                standardAmt = (int) Math.floor(difference / numGaps );
                extraSpaces = difference % numGaps;
                int inserted = 0;  
                for (int j = 0; j < numGaps; j++){        
                    String spaces = " ".repeat(standardAmt);
                    sb.insert(spaceIndices.get(j+zeroInd) + inserted, spaces);
                    inserted += standardAmt;
                    if (extraSpaces > 0 ){
                        sb.insert(spaceIndices.get(j+zeroInd) +inserted, " ");
                        extraSpaces--;
                        inserted++;
                    }
                }
                returnList.add(sb.toString());
            }
            else {
                difference = maxWidth - length;
                String spaces = " ".repeat(difference);
                sb.append(spaces);
                returnList.add(sb.toString());
                continue;
            }
        }
        return returnList;
    }
}