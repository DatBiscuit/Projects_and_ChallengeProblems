import java.util.Random;
import java.util.Scanner;

// 0 is rock
// 1 is paper 
// 2 is scissors

public class rps {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Random r = new Random();
        int computers_choice = r.nextInt(2);
        System.out.println("Type 0 for rock, 1 for paper and 2 for scissors ");
        int players_choice = sc.nextInt();

        System.out.print("Computer choice was: ");
        System.out.print(computers_choice);
        System.out.println();

        if(players_choice == computers_choice) {
            System.out.println("Draw!");
        }

        else if(players_choice == 0) {
            if(computers_choice == 1) {
                System.out.println("Computer won!");
            } else {
                System.out.println("You win!");
            }
        }

        else if(players_choice == 1) {
            if(computers_choice == 0) {
                System.out.println("You win!");
            } else {
                System.out.println("Computer won!");
            }
        }

        else if(players_choice == 2) {
            if(computers_choice == 0) {
                System.out.println("Computer won!");
            }
            else {
                System.out.println("You won!");
            }
        }
    }
}