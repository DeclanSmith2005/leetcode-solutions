class Solution {
    public String intToRoman(int num) {

        String returnString = "";
        int temp = num/1000;
        if ( temp >= 1){
            temp = (int) Math.floor(temp);
            num -= temp*1000;
            for (int i = 0; i <temp; i++ ){
                returnString= returnString.concat("M");
            }
            
        }
        if (num%900 == num-900){
            num-=900;
            returnString= returnString.concat("CM");
        }
        temp = num/500;
        if ( temp >= 1){
            temp =(int) Math.floor(temp);
            num -= temp*500;
            for (int i = 0; i <temp; i++ ){
               returnString= returnString.concat("D");
            }
            
        }
        if (num%400 == num-400){
            num-=400;
            returnString=returnString.concat("CD");
        }
        temp = num/100;
        if ( temp >= 1){
            temp = (int) Math.floor(temp);
            num -= temp*100;
            for (int i = 0; i <temp; i++ ){
                returnString=returnString.concat("C");
            }
            
        }
        if (num%90 == num-90){
            num-=90;
           returnString= returnString.concat("XC");
        }
        temp = num/50;
        if ( temp >= 1){
            temp = (int) Math.floor(temp);
            num -= temp*50;
            for (int i = 0; i <temp; i++ ){
              returnString=  returnString.concat("L");
            }
            
        }
        if (num%40 == num-40){
            num-=40;
           returnString= returnString.concat("XL");
        }
        temp = num/10;
        if ( temp >= 1){
            temp = (int) Math.floor(temp);
            num -= temp*10;
            for (int i = 0; i <temp; i++ ){
                returnString=returnString.concat("X");
            }
            
        }
        if (num%9 == num-9){
            num-=9;
            returnString=returnString.concat("IX");
        }
        temp = num/5;
        if ( temp >= 1){
            temp = (int) Math.floor(temp);
            num -= temp*5;
            for (int i = 0; i <temp; i++ ){
                returnString= returnString.concat("V");
            }
            
        }
        if (num%4 == num-4){
            num-=4;
            returnString= returnString.concat("IV");
        }
        temp = num/1;
        if ( temp >= 1){
            temp = (int) Math.floor(temp);
            num -= temp*1;
            for (int i = 0; i <temp; i++ ){
                returnString= returnString.concat("I");
            }
            
        }
        return returnString;
    }
}