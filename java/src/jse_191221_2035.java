import java.util.Stack;

public class jse_191221_2035 {

    public static void main(String[] args) {
        evaluate("3 4 -");
    }

    /**
     * CodeWars: Reverse polish notation calculator
     * https://www.codewars.com/kata/reverse-polish-notation-calculator/java
     */
    public static double evaluate(String expr) {
        if (expr.isEmpty())
            return 0.0;
        Stack<Double> operands = new Stack<>();
        for (String token : expr.split(" ")) {
            switch (token) {
                case "+":
                    operands.push(operands.pop() + operands.pop());
                    break;
                case "-":
                    operands.push(-operands.pop() + operands.pop());
                    break;
                case "*":
                    operands.push(operands.pop() * operands.pop());
                    break;
                case "/":
                    operands.push(1.0 / operands.pop() * operands.pop());
                    break;
                default:
                    operands.push(Double.parseDouble(token));
            }
        }
        return operands.pop();
    }
}
