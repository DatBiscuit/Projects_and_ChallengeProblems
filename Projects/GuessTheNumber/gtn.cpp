#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <ctime>

using namespace std;

int main() {
    srand((unsigned) time(0));
    int guesses = 3;
    int playerGuess;
    int randomNumber = (rand() % 10) + 1;

    while (guesses > 0) {
        cout << "Guess a number between 1-10" << endl;
        cin >> playerGuess;
        if(playerGuess == randomNumber) {
            cout << "You are correct!" << endl;
            break;
        } else {
            cout << "Sorry that is incorrect" << endl;
            guesses--;
        }

    }

    if(guesses == 0) {
        cout << "Game Over! The correct number was: " << randomNumber << endl;
    }
}