import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

@FunctionalInterface
interface CallableArithmetic {
    Integer evaluate(int a, int b);
}

public class jse_191230_2356 {

    public static void main(String[] args) {
        rowWeights(new int[]{90, 10, 120, 10});
        System.out.println(arithmetic(8, 2, "subtract"));
        System.out.println(extractFileName("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"));
    }

    /**
     * CodeWars: Row Weights
     * https://www.codewars.com/kata/row-weights/java
     */
    public static int[] rowWeights(final int[] weights) {
        int weightOne, weightTwo;
        weightOne = weightTwo = 0;
        for (int i = 0; i < weights.length; i++) {
            if ((i + 1) % 2 == 1) {
                weightOne += weights[i];
            } else {
                weightTwo += weights[i];
            }
        }
        return new int[]{weightOne, weightTwo}; // Do your magic!
    }

    /**
     * CodeWars: Make a function that does arithmetic!
     * https://www.codewars.com/kata/make-a-function-that-does-arithmetic/java
     */
    public static int arithmetic(int a, int b, String operator) {
        CallableArithmetic add, subtract, multiply, divide;
        Map<String, CallableArithmetic> actions = new HashMap<>();

        add = (numOne, numTwo) -> numOne + numTwo;
        subtract = (numOne, numTwo) -> numOne - numTwo;
        multiply = (numOne, numTwo) -> numOne * numTwo;
        divide = (numOne, numTwo) -> numOne / numTwo;
        actions.put("add", add);
        actions.put("subtract", subtract);
        actions.put("multiply", multiply);
        actions.put("divide", divide);

        return actions.get(operator).evaluate(a, b);
    }

    /**
     * CodeWars: extract file name
     * https://www.codewars.com/kata/extract-file-name/java
     */
    public static String extractFileName(String dirtyFileName) {
        final Pattern PATTERN = Pattern.compile("\\d*\\_(.+)\\.\\S*");
        Matcher matcher = PATTERN.matcher(dirtyFileName);

        if (matcher.find()) {
            return matcher.group(1);
        }
        throw new RuntimeException("Couldn't find file name");
    }
}
