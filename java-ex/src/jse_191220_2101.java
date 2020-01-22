import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class jse_191220_2101 {

    public static void main(String[] args) {
        countBits(1234);
        System.out.println(twoSort(new String[]{"bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"}));
    }

    /**
     * CodeWars: Bit Counting
     * https://www.codewars.com/kata/bit-counting/java
     */
    public static int countBits(int n) {
        int count = 0;
        while (n > 0) {
            if (n % 2 > 0)
                count++;
            n = n / 2;
        }
        return count;
    }

    public static int countBitsStream(int n) {
        return (int) Integer.toBinaryString(n).chars()
                .filter(c -> c == '1')
                .count();
    }

    /**
     * CodeWars: Sort and Star
     * https://www.codewars.com/kata/sort-and-star/java
     */
    public static String twoSort(String[] s) {
        List<String> list = new ArrayList<>(Arrays.asList(s));
        List<String> tmp = new ArrayList<>();
        Collections.sort(list);
        char[] chars = list.get(0).toCharArray();
        for (Character c : chars) {
            tmp.add(String.valueOf(c));
        }
        return tmp.stream().collect(Collectors.joining("***"));
    }
}
