import java.util.Scanner;

public class NumberGame2 {
    int Number = (int) (Math.random() * 100); //Gets a random number from 0 to 100
    Scanner myObj = new Scanner(System.in);

    public void guess(String guessNumber){
        System.out.println("What is your " + guessNumber + " guess?");
        int Guess = myObj.nextInt();
        if (Guess == Number) {
            System.out.println("You got it, awesome job!");
            System.exit(0);
        } else if (Guess > Number) {
            System.out.println("The number is LOWER than your guess, try again!");
        } else if (Guess < Number) {
            System.out.println("The number is HIGHER than your guess, try again!");
        }
    }   public static void main(String[] args) {
        Scanner myNum = new Scanner(System.in);
        System.out.println("Would you like to play higher or lower? Please answer 1 for yes, and 2 for no.");
        
        int YesOrNo = myNum.nextInt();
        if (YesOrNo == 1){
            System.out.println("let's play! Guess a number from 1 to 100.");
        } else if (YesOrNo == 2) {
            System.out.println("No problem, have a good day!");
            System.exit(0);
        }
    
        NumberGame2 game = new NumberGame2();
        game.guess("first");
        game.guess("second");   
        game.guess("third");
        System.out.println("Sorry, the number was " + game.Number + "!");
    }   
}