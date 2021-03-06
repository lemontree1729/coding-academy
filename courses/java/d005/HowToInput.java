package d005;

import java.util.Scanner; // use Scanner to get standard input

class HowToInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // Can construct with both String and InputStream.
        // Press enter will end the input with including the newline
        while (sc.hasNext()) { // boolean condition
            System.out.println(sc.next().substring(0, 1)); // print first chr for each word
        }
        sc.close(); // java recommends closing the Scanner when its work is done
    }
}
