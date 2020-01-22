import java.util.ArrayList;
import java.util.List;

public class jse_191207_1755 {

    public static void main(String[] args) {
        System.out.println(calculateYears(1000, 0.05, 0.18, 1000));
        System.out.println(bouncingBall(30.0, 0.66, 1.5));
        System.out.println(new jse_191207_1755().spinWords("Hey fellow warriors"));
        reverseWord("EtOH = c2h5oh");
    }

    /**
     * CodeWars: Money, Money, Money
     * https://www.codewars.com/kata/money-money-money/java
     */
    public static int calculateYears(double principal, double interest, double tax, double desired) {
        double profit = 0;
        int years = 0;
        while (principal < desired) {
            profit = principal * interest;
            principal = profit - profit * tax + principal;
            years++;
        }
        return years;
    }

    /**
     * CodeWars: Bouncing Balls
     * https://www.codewars.com/kata/bouncing-balls/train/java
     */
    public static int bouncingBall(double h, double bounce, double window) {
        double newHeight = h;
        int count = 0;
        if ((h <= 0) || (bounce <= 0) || (bounce >= 1) || (window >= h)) return -1;
        while (newHeight > window) {
            newHeight *= bounce;
            count += 2;
        }
        return count - 1;
    }

    /**
     * Two methods to reverse a word by StringBuilder
     */
    private static void reverseWord(String word) {
        // StringBuild.reverse()
        System.out.println(new StringBuilder(word).reverse().toString());

        // Add char one by one iteration method
        StringBuilder reversed = new StringBuilder();
        char[] chars = word.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            reversed.append(chars[chars.length - i - 1]);
        }
        System.out.println(reversed.toString());
    }

    /**
     * CodeWars: Stop gninnipS My sdroW!
     * https://www.codewars.com/kata/stop-gninnips-my-sdrow/java
     */
    public String spinWords(String sentence) {
        List<String> wordList = new ArrayList<>();
        String word = "";
        for (String s : sentence.split(" ")) {
            word = s.length() > 4 ? new StringBuilder(s).reverse().toString() : s;
            wordList.add(word);
        }
        return String.join(" ", wordList);
    }

}
