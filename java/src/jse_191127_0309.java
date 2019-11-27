import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Java 8 Groussard: Mise en œuvre avec Java.
 * Calculator that parses expression with Regex.
 * Switch causes are implemented with the Command Design Pattern.
 * Based on the previous task - jse_191126_2031
 */
public class jse_191127_0309 {
    private static final String EXAMPLE = "5+ 12=";

    public static void main(String[] args) {
        Expression exp = new Expression(EXAMPLE);
        ExpressionParser parser = new ExpressionParser(exp);
        CalculationCommand command = new CalculationCommand();

        exp = parser.getExpression();
        String text = String.format(
                "Expression: %d %c %d = %d",
                exp.getNumberOne(),
                exp.getOperator(),
                exp.getNumberTwo(),
                command.calculate(exp)
        );
        System.out.println(text);
    }
}

/**
 * Store numbers, operator and a whole expression string
 */
class Expression {

    public String rawExpression;
    private String parsedExpression;
    private Integer numberOne;
    private Integer numberTwo;
    private Character operator;

    Expression() {
        this.numberOne = this.numberTwo = 0;
        this.operator = null;
    }

    Expression(String expression) {
        this.rawExpression = expression;
    }

    Expression(Integer numberOne, Integer numberTwo, Character operator) {
        setNumbers(numberOne, numberTwo, operator);
    }

    void setNumbers(Integer numberOne, Integer numberTwo, Character operator) {
        this.numberOne = numberOne;
        this.numberTwo = numberTwo;
        this.operator = operator;
    }

    Integer getNumberOne() {
        return numberOne;
    }

    Integer getNumberTwo() {
        return numberTwo;
    }

    Character getOperator() {
        return operator;
    }

    public String getParsedExpression() {
        return parsedExpression;
    }

    public void setParsedExpression(String expression) {
        this.parsedExpression = expression;
    }
}

/**
 * Find numbers and operators within an expression
 */
class ExpressionParser {

    private static final String PATTERN = "(\\d+)\\s*([\\+\\-\\*\\/]{1})\\s*(\\d+)";

    private Expression expressionObj;
    private String expressionString, e;
    private Integer a, b;
    private Character o;
    private Pattern patternObj;
    private Matcher matcherObj;

    ExpressionParser() {
    }

    ExpressionParser(Expression expressionObj) {
        this.expressionObj = expressionObj;
        this.expressionString = expressionObj.rawExpression;
    }

    private void parseExpression() {
        this.patternObj = Pattern.compile(PATTERN);
        this.matcherObj = patternObj.matcher(expressionString);

        if (matcherObj.find()) {
            this.e = matcherObj.group(0);
            this.a = Integer.parseInt(matcherObj.group(1));
            this.o = matcherObj.group(2).charAt(0);
            this.b = Integer.parseInt(matcherObj.group(3));
        }
    }

    Expression getExpression() {
        parseExpression();
        expressionObj.setNumbers(a, b, o);
        expressionObj.setParsedExpression(e);
        return expressionObj;
    }

    void testFindGroups() {
        for (int i = 0; i < matcherObj.groupCount(); i++) {
            System.out.println(matcherObj.group(i + 1));
        }
    }
}

@FunctionalInterface
interface Commandable {
    Integer eval(Integer a, Integer b);
}

/**
 * Choose a method implementation according to the given operator
 */
class CalculationCommand {

    private final Map<Character, Commandable> ACTIONS;
    private final Map<Character, Commandable> actions;
    private Commandable add, substract, multiply, divide;

    CalculationCommand() {
        actions = new HashMap<>();
        add = Integer::sum;
        substract = (a, b) -> a - b;
        multiply = (a, b) -> a * b;
        divide = (a, b) -> {
            if (b == 0) {
                throw new IllegalArgumentException("Divided by zero");
            }
            return (Integer) a / b;
        };

        actions.put('+', add);
        actions.put('-', substract);
        actions.put('*', multiply);
        actions.put('/', divide);

        ACTIONS = Collections.unmodifiableMap(actions);
    }

    public Map<Character, Commandable> getActions() {
        return ACTIONS;
    }

    public Commandable getCommand() {
        return ACTIONS.get(null);
    }

    public Integer calculate(
            Character operator, Integer numOne, Integer numTwo) {
        Commandable command = ACTIONS.get(operator);
        return command.eval(numOne, numTwo);
    }

    public Integer calculate(Expression expression) {
        Character operator = expression.getOperator();
        Integer numOne = expression.getNumberOne();
        Integer numTwo = expression.getNumberTwo();
        return this.calculate(operator, numOne, numTwo);
    }
}
