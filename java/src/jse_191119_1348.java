import java.util.Scanner;

public class jse_191119_1348 {

    public static void main(String[] args) {
//        showCarBoolean();
//        showRemainder();
        showTemperature();
    }

    private static void showTemperature() {
        Double fahr;
        Double cel;
        Scanner in;

        in = new Scanner(System.in);
        System.out.println("Enter the temperature in F: ");
        fahr = in.nextDouble();

        cel = (fahr - 32) * 5.0 / 9.0;
        System.out.println("The temperature in C is: " + cel);

        System.exit(0);
    }

    private static void showCarBoolean() {
        boolean isCar = false;
        if (isCar) {
            System.out.println("isCar isn't true");
        }

        isCar = true;
        boolean wasCar = isCar ? true : false;
        if (wasCar) {
            System.out.println("wasCar is true");
        }
    }

    private static void showRemainder() {
        double firstValue = 20.00d;
        double secondValue = 80.00d;
        double total = ((firstValue + secondValue) * 100.00d);
        double remainder = total % 40.00d;
        boolean isNoRemainder = remainder == 0 ? true : false;
        System.out.println("Remainder doesn't exist: " + isNoRemainder);
        if (!isNoRemainder) {
            System.out.println("Got some remainder");
        }
    }
}
