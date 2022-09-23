import java.util.Scanner;

class Main {
  public static void main(String[] args) {

    /*
     * Integer division
     * Precedence
     * Closing the scanner class
     * Combined assignment operators
     * Strings - difference between equals and compare to
     * Logical operators
     * ! Operator, Precedence, parenthesis
     * Decision Structures
     */
    // int a, b, c = 0;
    // double rslt = 0;
    // rslt = (double) x / (double) y;
    // print(rslt);
    // String k = "Hello";
    // String l = "Zello";
    // print(k==l);
    // print(k.compareTo(l));
    // for (int i = 9; i>-1; i--) {
    // System.out.println(i);
    // }
    // create var for userChoic. WIll update with each sanner.in 
    // System.out.println(userChoice);
    // while(!userChoice.equals("Q")){
    // System.out.println("You havn't entered q yet");
    // userChoice = input.nextLine();
    // System.out.println("You entered..." + userChoice);
    // }
    // do {
    // getInput();
    // }while(!userChoice.equals("Q"));
    System.out.println(validate(9));
  }

  // This method returns the scanner nextLine to the caller. No input.
  private static String input() {
    Scanner input = new Scanner(System.in);
    return input.nextLine();
  }

  // args: a number as int to validate.
  // returns: true if arg is <0 wefsdf
  // Created to avoid repeating code block.
  private static boolean validate(int testMe) {
    if (testMe >= 0 && testMe <= 10) {
      // number is in range return true.
      return true;
    }
    // this will run when if statemetns only. in that case number is not in range. return false. 
    return false;
  }

  // public static void print(String valueToPrint) {
  // System.out.println(valueToPrint);
  // }

  // public static void print(int valueToPrint) {
  // System.out.println(valueToPrint);
  // }

  // public static void print(double valueToPrint) {
  // System.out.println(valueToPrint);
  // }

  // public static void print(boolean valueToPrint) {
  // System.out.println(valueToPrint);
  // }

  // as many runs as defined. From x to y
  // for

  // as long as a condition is met
  // while

  // runs at least once, then as as long as a condition is met.
  // do while loop

}