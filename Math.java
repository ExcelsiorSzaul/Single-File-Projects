import java.util.InputMismatchException;
import java.util.Scanner;
import java.text.DecimalFormat;

public class Math {
    public static double add(double a, double b) { // Adds two numbers
        return a+b;
    }
    public static double subtract(double a, double b) { // Subtracts two numbers
        return a-b;
    }
    public static double multiply(double a, double b) { // Multiplies two numbers
        return a*b;
    }
    public static double divide(double a, double b) { // Divides two numbers
        // Catches Divide By Zero
        if (b == 0) {
            System.out.println("Error: Cannot Divide By Zero");
            return 0;
        }
        return a/b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#0.00");
        double number1 = 0;
        double number2 = 0;
        while (true) {
            try {
                System.out.print("Enter A Number: ");
                number1 = scanner.nextFloat();
                System.out.print("Enter Another Number: ");
                number2 = scanner.nextFloat();
                scanner.nextLine();
            } catch (InputMismatchException e) {
                System.out.println("Error: Please Enter Integers Only");
                scanner.nextLine();
                continue;
            }

            double sum = add(number1, number2);
            double diff = subtract(number1, number2);
            double product = multiply(number1, number2);
            double quotient = divide(number1, number2);

            System.out.println("The Sum is: " + df.format(sum));
            System.out.println("The Difference is: " + df.format(diff));
            System.out.println("The Product is: " + df.format(product));
            System.out.println("The Quotient is: " + df.format(quotient));

            System.out.print("Would You Like To Quit? ('y' to quit): ");
            String confirm = scanner.nextLine();
            if (confirm.equalsIgnoreCase("y")) {
                break;
            }
        }
        scanner.close();
    }
}