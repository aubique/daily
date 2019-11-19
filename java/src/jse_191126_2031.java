import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

/**
 * Java 8 Groussard: Mise en œuvre avec Java
 * Implementing the Command Design Pattern
 * Which is designed herewith by anonymous class methods and lambda expressions
 */
public class jse_191126_2031 {

    public static void main(String[] args) {
        Character exp = '/';
        Integer a = 13;
        Integer b = 6;
        CommandAction calc = new CommandAction();
        Integer result = calc.getCalculation(exp, a, b);
        System.out.printf("Expression:%n%d %c %d = %d", a, exp, b, result);
    }

}

interface Command {

    Integer calculate(Integer a, Integer b);
}

class CommandAction {

    private static final Map<Character, Command> ACTIONS;

    static {
        final Map<Character, Command> actions = new HashMap<>();
        Command substract = (a, b) -> a - b;

        actions.put('+', (a, b) -> a + b);

        actions.put('-', substract);

        actions.put('*', new Command() {
            @Override
            public Integer calculate(Integer a, Integer b) {
                return a * b;
            }
        });

        actions.put('/', new Command() {
            @Override
            public Integer calculate(Integer a, Integer b) {
                if (b == 0) {
                    throw new IllegalArgumentException("Divide by zero");
                }
                return (Integer) a / b;
            }
        });

        ACTIONS = Collections.unmodifiableMap(actions);
    }

    public Integer getCalculation(Character actionType, Integer numOne, Integer numTwo) {

        Command operation = ACTIONS.get(actionType);
        return operation.calculate(numOne, numTwo);
    }
}
