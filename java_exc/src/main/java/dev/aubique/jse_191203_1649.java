package dev.aubique;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class jse_191203_1649 {

    public static void main(String[] args) {
//        System.out.println(solution("world"));
//        System.out.println(findNeedle(new Object[]{"hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"}));
        System.out.println(ConvertBinaryArrayToInt(new ArrayList<>(Arrays.asList(1, 1, 1, 1))));
    }

    /**
     * CodeWars: Reversed Strings
     * https://www.codewars.com/kata/reversed-strings/java
     */
    public static String solution(String str) {
        StringBuilder reversed = new StringBuilder();
        for (int i = str.length(); i > 0; i--) {
            reversed.append(str.charAt(i - 1));
        }
        return reversed.toString();
    }

    /**
     * CodeWars: A Needle in the Haystack
     * https://www.codewars.com/kata/a-needle-in-the-haystack/java
     */
//    public static String findNeedle(Object[] haystack) {
//        Object needle = (Object) "needle";
//        for (int i = 0; i < haystack.length; i++) {
//            if ((haystack[i] != null) && (haystack[i].equals(needle))) {
//                return "found the needle at position " + i;
//            }
//        }
//        return "";
//    }
    public static String findNeedle(Object[] haystack) {
        return String.valueOf(java.util.Arrays.asList(haystack).indexOf("needle"));

    }

    /**
     * CodeWars: Ones and Zeros
     * https://www.codewars.com/kata/ones-and-zeros/java
     */
    public static int ConvertBinaryArrayToInt(List<Integer> binary) {
        int power, converted = 0;
        for (int i = 0, j = binary.size() - 1; j >= 0; i++, j--) {
            converted += Math.pow(2, i) * binary.get(j);
        }
        return converted;
    }
}
