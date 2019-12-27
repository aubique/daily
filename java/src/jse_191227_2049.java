import java.util.*;

public class jse_191227_2049 {

    public static void main(String[] args) {
        String pangram1 = "The quick brown fox jumps over the lazy dog.";
        System.out.println(check(pangram1));
    }

    /**
     * CodeWars: Detect Pangram
     * https://www.codewars.com/kata/detect-pangram/java
     */
    public static boolean check(String sentence) {
        final Character[] SIGNS = {'!', '?', '.', ',', ' '};
        List<Character> alphabet = new ArrayList<>(26);
        for (int i = 0; i < 26; i++) {
            alphabet.add((char) (i + 96));
        }
        final Set<Character> ALPHABET_SET = new HashSet<>(alphabet);
        Set<Character> sentenceChars = new HashSet<>();

        if (!sentence.isEmpty()) {
            for (Character c : sentence.toCharArray()) {
                if (!Arrays.asList(SIGNS).contains(c)) {
                    sentenceChars.add(c);
                }
            }

            if (ALPHABET_SET.size() <= sentenceChars.size())
                return true;
        }
        return false;
    }

}
