import java.util.Scanner;

public class Reverse {
    public static void main(String[] args) {
        // Collect a string from user, reverse it, and print the original and reversed string
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Please Enter A String To Reverse: ");
            String original = scanner.nextLine();
            String reversed = reverseString(original);
            System.out.println("Original: " + original);
            System.out.println("Reversed: " + reversed);
            System.out.println("Would you like to choose another string (y/n): ");
            String confirm = scanner.nextLine();
            if (!confirm.equalsIgnoreCase("y")) {
                break;
            }
        }
        scanner.close();
    }

    public static String reverseString(String str) {
        // Check For Empty Or Null String
        if (str == null || str.length() == 0) {
            return str;
        }

        // Convert str to a character array and select left and right characters
        char[] charArray = str.toCharArray();
        int left = 0;
        int right = charArray.length - 1;

        // Move left and right towards each other while switching their positions
        while (left < right) {
            char temp = charArray[left];
            charArray[left] = charArray[right];
            charArray[right] = temp;
            left++;
            right--;
        }
        
        // Return the reversed char array as a string
        return new String(charArray);
    }
}
