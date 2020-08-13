#include <stdio.h>
#include <stdlib.h>
#include <ctime>
#include <iostream>

using namespace std;

int main() {
    srand((unsigned) time(0));
    int players_choice;
    int computers_choice = rand() % 3;
    cout << "Type 0 for rock, 1 for paper, or 2 for scissors" << endl;
    cin >> players_choice;
    cout << "Computer choice was: " << computers_choice << endl;

    
        if(players_choice == computers_choice) {
            cout << "Draw!" << endl;
        }

        else if(players_choice == 0) {
            if(computers_choice == 1) {
                cout << "Computer won!" << endl;
            } else {
                cout << "You win!" << endl;
            }
        }

        else if(players_choice == 1) {
            if(computers_choice == 0) {
                cout << "You win!" << endl;
            } else {
                cout << "Computer won!" << endl;
            }
        }

        else if(players_choice == 2) {
            if(computers_choice == 0) {
                cout << "Computer won!" << endl;
            }
            else {
                cout << "You won!" << endl;
            }
        }
}