import java.util.Random;
import java.util.Scanner;

public class gtn {
    public static void main(String args[]) {
        int guesses = 3;
        Random random = new Random();
        Scanner sc = new Scanner(System.in);
        int randomNumber = random.nextInt(9) + 1;

        while (guesses > 0) {
            System.out.println("Guess a number between 1-10");
            int playerGuess = sc.nextInt();
            if(playerGuess == randomNumber) {
                System.out.println("You are correct!");
                break;
            } else {
                System.out.println("Sorry that is incorrect");
                guesses--;
            }

        }

        if(guesses == 0) {
            System.out.print("Game Over! The correct number was: ");
            System.out.print(randomNumber);
        }
    }
}