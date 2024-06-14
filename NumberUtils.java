public class NumberUtils {

    public static int addNumbers(Integer a, Integer b) {
        if (a == null || b == null) {
            return 0;
        }
        return a + b;
    }

    public static void main(String[] args) {
        // Example usage:
        System.out.println(addNumbers(3, 5));   // Output: 8
        System.out.println(addNumbers(null, 5)); // Output: 0
        System.out.println(addNumbers(3, null)); // Output: 0
        System.out.println(addNumbers(null, null)); // Output: 0
    }
}
