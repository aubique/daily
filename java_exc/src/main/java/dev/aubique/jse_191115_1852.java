package dev.aubique;

import java.util.Scanner;

public class jse_191115_1852 {

    public static void main(String[] args) {
//        showPersonalInfo();
        showFahrenheit();
    }

    private static void showPersonalInfo() {
        Scanner input = new Scanner(System.in);
        String nameMessage = "What's your name?";
        String ageMessage = "How old are you?";
        String birthdayMessage = "When have you been born?";
        String locationMessage = "Where do you live?";
        int userAge = 0;

        System.out.println(nameMessage);
        String userName = input.nextLine();

        System.out.println(ageMessage);
        try {
            userAge = Integer.parseInt(input.nextLine());
        } catch (NumberFormatException e) {
            e.printStackTrace();
        }

        System.out.println(birthdayMessage);
        String userBirthday = input.nextLine();

        System.out.println(locationMessage);
        String userLocation = input.nextLine();

        System.out.println("Your name: " + userName);
        System.out.println("Your age: " + userAge);
        System.out.println("Your birthday: " + userBirthday);
        System.out.println("Your address: " + userLocation);
    }

    private static int calculateThreeNumbers(int num1, int num2, int num3) {
        return (num1 * num2) / num3;
    }

    private static void showFahrenheit() {
        Scanner input = new Scanner(System.in);

        System.out.println("Type the current degree Celsuis");
        int degree = getFahrenheit(input.nextDouble());
        System.out.println("The Fahrenheit converted temperature degree is " + degree);
    }

    private static int getFahrenheit(double celsuis) {
        return (int) ((9 / 5) * celsuis + 34);
    }
}
