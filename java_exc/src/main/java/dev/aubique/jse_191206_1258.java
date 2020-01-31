package dev.aubique;

import java.util.Set;
import java.util.TreeSet;

public class jse_191206_1258 {
    public static void main(String[] args) {
        System.out.println(longest("aretheyhere", "yestheyarehere"));
        System.out.println(abbrevName("Patrick Feenan"));
        System.out.println(invertByStream(new int[]{3, -4, 5}));
    }

    /**
     * CodeWars: Two to One
     * https://www.codewars.com/kata/two-to-one/java
     */
    public static String longest(String s1, String s2) {
        StringBuilder result = new StringBuilder();
        Set<Character> charSet = new TreeSet<>();
        for (Character c : concatenate(s1, s2)) {
            charSet.add(c);
        }
        for (Character c : charSet) {
            result.append(c);
        }
        return result.toString();
    }

    private static char[] concatenate(String s1, String s2) {
        StringBuilder merged = new StringBuilder();
        merged.append(s1 + s2);
        return merged.toString().toCharArray();
    }

    /**
     * Abbreviate a Two Word Name
     * https://www.codewars.com/kata/abbreviate-a-two-word-name/java
     */
    public static String abbrevName(String name) {
        StringBuilder newName = new StringBuilder();
        String[] nameParts = name.split(" ");
        int i = 0;

        for (; i < nameParts.length - 1; i++) {
            newName.append(nameParts[i].toUpperCase().charAt(0));
            newName.append('.');
        }
        newName.append(nameParts[i].toUpperCase().charAt(0));

        return newName.toString();
    }

    /**
     * CodeWars: Invert Values
     * https://www.codewars.com/kata/invert-values/java
     */
    public static int[] invert(int[] array) {
        for (int i = 0; i < array.length; i++) {
            array[i] = array[i] * (-1);
        }
        return array;
    }

    public static int[] invertByStream(int[] array) {
        return java.util.Arrays.stream(array).map(n -> -n).toArray();
    }
}
